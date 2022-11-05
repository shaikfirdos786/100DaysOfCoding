from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

YELLOW = "#f7f5dd"


# --------------------------------Password Generator-----------------------------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------Save Password-------------------------------#

def save():
    website_input = website_entry.get()
    email_username_input = email_username_entry.get()
    password_input = password_entry.get()

    if len(website_input) == 0 or len(email_username_input) == 0 or len(password_input) == 0:
        messagebox.showwarning(title="Oops! Empty field", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_input,
                                       message=f"These are the details entered:\n Website: {website_input}\n "
                                               f"Email_User: {email_username_input}\n Password: {password_input}\n "
                                               f"Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(
                    f"Website: {website_input} | User/Email: {email_username_input} | Password: {password_input} \n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                website_entry.focus()


# ----------------------------UI Setup--------------------------#

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", highlightthickness=0, bg=YELLOW)
email_username_label = Label(text="Email/Username:", highlightthickness=0, bg=YELLOW)
password_label = Label(text="Password:", highlightthickness=0, bg=YELLOW)
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35, highlightthickness=0)
email_username_entry = Entry(width=35, highlightthickness=0)
password_entry = Entry(width=21, highlightthickness=0)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry.grid(row=2, column=1)
email_username_entry.insert(0, "fidduraza9876@gmail.com")
password_entry.grid(column=1, row=3)

# Buttons

generate_pass_button = Button(text="Generate Password", command=generate_password, highlightthickness=0, bg="#D8E9A8")
add_button = Button(text="Add", width=36, command=save, highlightthickness=0, bg="#ECB365")
generate_pass_button.grid(column=2, row=3)
add_button.grid(row=4, column=1)

window.mainloop()
