from tkinter import * # Will import all the classes
from tkinter import messagebox # This module must be imported
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    final_password = ''.join(password_list)
    pyperclip.copy(final_password) # This line of code will copy the password to the clipboard
    password_entry.insert(0,final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message= " Please don't have any fields empty. ")
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save ?")
        if is_ok:
            with open("./day_29/data.txt", mode='a') as data:
                data.write(f"Website: {website} ; Username: {email}; Password: {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
lock_icon = PhotoImage(file = './day_29/logo.png')
canvas = Canvas(height = 200, width = 200, highlightthickness = 0)
canvas.create_image(100, 100, image = lock_icon)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column = 0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column = 0)

password_label = Label(text="Password:")
password_label.grid(row=3, column = 0)

# Entries
website_entry = Entry(width = 50)
website_entry.grid(row=1, column = 1, columnspan=2)
website_entry.focus() # This line of code will automatically focus the cursor on the website entry field

email_entry = Entry(width = 50)
email_entry.grid(row=2, column = 1, columnspan=2)
email_entry.insert(0,"ahamedbasheer2002@gmail.com") # This line of code will automatically insert the email address in the email entry field

password_entry = Entry(width = 32, highlightthickness= 0)
password_entry.grid(row=3, column = 1)

generate_button = Button(text='Generate Password', width = 15, command=generate_password)
generate_button.grid(row=3, column = 2)

add_button = Button(text='Add', width = 43, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()