from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BLACK = "#404258"
RED = "#FF0000"
GRAY = "#787A91"
SKIN = "#F9F9F9"
BLUE = "#3120E0"


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
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops! Empty field", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ------------------------------Find Password--------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ----------------------------UI Setup--------------------------#

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg=BLACK)

canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", highlightthickness=0, bg=BLACK, fg=RED)
email_username_label = Label(text="Email/Username:", highlightthickness=0, bg=BLACK, fg=RED)
password_label = Label(text="Password:", highlightthickness=0, bg=BLACK, fg=RED)
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35, highlightthickness=0, bg=SKIN)
email_username_entry = Entry(width=35, highlightthickness=0, bg=SKIN)
password_entry = Entry(width=35, highlightthickness=0, bg=SKIN)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry.grid(row=2, column=1)
email_username_entry.insert(0, "fidduraza9876@gmail.com")
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=14, highlightthickness=0, command=find_password, fg=RED, bg=GRAY)
generate_pass_button = Button(text="Generate Password", command=generate_password, highlightthickness=0, bg=GRAY,
                              fg=RED)
add_button = Button(text="Add", width=36, command=save, highlightthickness=0, bg=GRAY, fg=RED)
search_button.grid(row=1, column=2)
generate_pass_button.grid(column=2, row=3)
add_button.grid(row=4, column=1)

window.mainloop()
