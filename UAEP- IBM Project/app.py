import pickle
import sqlite3
import streamlit as st
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def authenticate(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    
    if user and check_password_hash(user['password'], password):
        return True, user['name']
    return False, None

# Signup form for new users
def signup_form():
    st.subheader("Sign Up")
    with st.form("Signup"):
        name = st.text_input("Full Name")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Sign Up")
        
        if submitted:
            if password != confirm_password:
                st.error("Passwords do not match!")
                return
            
            hashed_password = generate_password_hash(password)
            conn = get_db_connection()
            try:
                conn.execute(
                    'INSERT INTO users (name, username, password) VALUES (?, ?, ?)',
                    (name, username, hashed_password)
                )
                conn.commit()
                st.success("Account created successfully! Please log in.")
            except sqlite3.IntegrityError:
                st.error("Username already exists. Please choose a different username.")
            finally:
                conn.close()

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

# Load dataset
def load_data():
    try:
        df = pd.read_csv('Dataset/Admission_Predict.csv')
        df.rename(columns=lambda x: x.strip(), inplace=True)  # Clean column names
        return df
    except Exception as e:
        st.error(f"Failed to load dataset: {str(e)}")
        return None


# Main Application
def main_app():
    
    try:
        logo = Image.open('images/logo.png')
        st.sidebar.image(logo, use_container_width=True)
    except FileNotFoundError:
        st.sidebar.warning("Logo image not found.")

    first_name = st.session_state['name'].split()[0]
    st.sidebar.title(f"Welcome {first_name}👋")
    
    # Load ML Model
    try:
        with open('model/model.pkl', 'rb') as file:
            model = pickle.load(file)
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return
    
    # Load dataset
    data_load_state = st.text('Loading admission dataset...')
    df = load_data()
    data_load_state.text('Loading admission dataset... Completed!')
    
    if df is None:
        return

    # Education Content Section
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
    
    # University Image
    try:
        univ_img = Image.open('images/univ.png')
        st.image(univ_img, 
                caption='Top Universities',
                use_container_width=True)
    except FileNotFoundError:
        st.warning("University image not found")

    st.markdown("## Exploratory Data Analysis")
    st.write("This section provides insights into the dataset. You can explore the data using various visualizations.")
    st.write("Use the sidebar to select different visualizations.")

    # Visualization 1: Correlation Heatmap
    if st.sidebar.checkbox("🔶 Correlation Heatmap"):
        st.subheader("Feature Correlation")
        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)


    # Distribution Plots
    if st.sidebar.checkbox("📈 Distribution Plot"):
        st.subheader("Feature Distributions")
        selected_col = st.selectbox("Select Feature", df.columns[:-1])
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        st.pyplot(fig)

    # Admission Trends
    if st.sidebar.checkbox("📊 Admission Trends (Scatter)"):
        st.subheader("Admission Chance Relationships")
        feature = st.selectbox("Select Feature to Compare", ['GRE Score', 'TOEFL Score', 'CGPA'])
        fig, ax = plt.subplots(figsize=(10,6))
        sns.scatterplot(data=df, x=feature, y='Chance of Admit', hue='Research', ax=ax)
        st.pyplot(fig)

    # Pairplot
    if st.sidebar.checkbox("🔁 Pairplot (Slow)"):
        st.subheader("Pairwise Relationships")
        with st.spinner("Generating pairplot..."):
            fig = sns.pairplot(df, hue='Research')
            st.pyplot(fig)

    # University Rating Analysis
    if st.sidebar.checkbox("🏫 University Rating Analysis"):
        st.subheader("University Rating Distribution")
        col1, col2 = st.columns(2)
        with col1:
            fig1, ax1 = plt.subplots(figsize=(8,8))
            df['University Rating'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
            st.pyplot(fig1)
        with col2:
            fig2, ax2 = plt.subplots(figsize=(8,6))
            sns.countplot(x='University Rating', data=df, ax=ax2)
            st.pyplot(fig2)
            
    # Prediction Section
    st.markdown("---")
    st.markdown("## University Admit Eligibility Predictor")
    
   # Input fields
    gre = st.number_input("GRE Score (0-340)", 0, 340, 300)
    toefl = st.number_input("TOEFL Score (0-120)", 0, 120, 100)
    sop = st.slider("SOP Score (0-5)", 0.0, 5.0, 3.5)
    lor = st.slider("LOR Score (0-5)", 0.0, 5.0, 4.0)
    cgpa = st.number_input("CGPA (0-10)", 0.0, 10.0, 9.0)
    univ_rank = st.slider("University Rank", 1, 5, 3)

    # Prediction Logic
    if st.button("Predict Admission Chances"):
        try:
            input_data = pd.DataFrame([[gre, toefl, univ_rank, sop, lor, cgpa]],
                                    columns=['GRE Score', 'TOEFL Score', 'University Rating', 
                                             'SOP', 'LOR ', 'CGPA'])

            prediction = model.predict(input_data)
            chance = float(prediction[0]) * 100  # Ensure numeric conversion

            st.subheader(f"Admission Chance: {chance:.1f}%")
                
            if chance >= 66.67:
                st.success("High chances! 🎉 Consider applying!")
            else:
                st.warning("Moderate/Low chances 💡 Keep improving!")
        
            img = Image.open('images/chance.png' if chance >= 66.67 else 'images/noChance.png')
            st.image(img, width=500)
            
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
    st.sidebar.title("Authentication")
    auth_option = st.sidebar.radio("Choose an option", ["Login", "Sign Up"])
    if auth_option == "Login":
        login_form()
    elif auth_option == "Sign Up":
        signup_form()
