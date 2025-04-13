import pickle
import sqlite3
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from werkzeug.security import check_password_hash

# Database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Authentication check
def authenticate(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    
    if user and check_password_hash(user['password'], password):
        return True, user['name']
    return False, None

# Login form
def login_form():
    with st.form("Login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            authenticated, name = authenticate(username, password)
            if authenticated:
                st.session_state['authenticated'] = True
                st.session_state['name'] = name
                st.rerun()
            else:
                st.error("Invalid username/password")
                
# Main Application
def main_app():
    first_name = st.session_state['name'].split()[0]
    st.sidebar.title(f"Welcome {first_name}👋")
    # Load ML Model
    try:
        with open('model/model.pkl', 'rb') as file:
            model = pickle.load(file)
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return
    
    
    # ------ New Education Content Section ------
    st.markdown("## The Importance of Higher Education")
    
    education_content = """
    Higher education plays a pivotal role in personal and societal development:
    
    - 🎯 **Career Advancement**: Degrees open doors to better job opportunities
    - 💡 **Knowledge Expansion**: Deepens understanding of specialized fields
    - 🌍 **Global Perspective**: Fosters cultural awareness and global citizenship
    - 🤝 **Networking Opportunities**: Connects you with professionals and mentors
    - 💰 **Economic Growth**: Educated populations drive national prosperity
    - 🔬 **Research Innovation**: Fuels technological and scientific breakthroughs
    """
    
    st.info(education_content)
    
    # Display university image
    try:
        univ_img = Image.open('images/univ.png')
        st.image(univ_img, 
                caption='Global Education Opportunities',
                use_container_width=True)
    except FileNotFoundError:
        st.warning("University image not found")

    # Application Interface
    st.title("University Admit Eligibility Predictor")
    
    # Input Fields
    gre = st.number_input("GRE Score (0-340)", 0, 340, 300)
    toefl = st.number_input("TOEFL Score (0-120)", 0, 120, 100)
    sop = st.slider("SOP Score (0-5)", 0.0, 5.0, 3.5)
    lor = st.slider("LOR Score (0-5)", 0.0, 5.0, 4.0)
    cgpa = st.number_input("CGPA (0-10)", 0.0, 10.0, 9.0)
    univ_rank = st.slider("University Rank", 1, 5, 3)

    # Prediction Logic
    if st.button("Predict"):
        try:
            input_data = pd.DataFrame([[gre, toefl, univ_rank, sop, lor, cgpa]],
                                    columns=['GRE Score', 'TOEFL Score', 'University Rating', 
                                             'SOP', 'LOR ', 'CGPA'])  

            prediction = model.predict(input_data)

            if isinstance(prediction, (pd.DataFrame, pd.Series, np.ndarray, list)):
                chance = float(prediction[0]) * 100
            else:
                chance = float(prediction) * 100

            st.subheader(f"Admission Chance: {chance:.1f}%")
            
            # Display result image
            if chance >= 66.67:
                st.success("High chances! Consider applying!")
                img = Image.open('images/chance.png')
            else:
                st.warning("Moderate/Low chances")
                img = Image.open('images/noChance.png')
            
            st.image(img, width=300)
            
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

# Application Flow Control
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if st.session_state['authenticated']:
    main_app()
    if st.sidebar.button("Logout"):
        st.session_state['authenticated'] = False
        st.rerun()
else:
    login_form()
