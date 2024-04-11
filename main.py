import json
from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json


# --------------------------------FIND PASSWORD --------------------------------- #
def find_password():
    lookup_data = web_site_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")

    else:
        if lookup_data in data:
            email = data[lookup_data]["email"]
            password = data[lookup_data]["password"]
            messagebox.showinfo(title=f"{lookup_data}", message=f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exist")
            

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    username = email_username_entry.get()
    website = web_site_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,

        }
    }

    if len(username) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="You are missing information, please check your inputs")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_site_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_site_label = Label(text="Website:")
web_site_label.grid(column=0, row=1)

web_site_entry = Entry(width=18)
web_site_entry.focus()
web_site_entry.grid(column=1, row=1, sticky="w")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=37)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
# Pre-set email
#email_username_entry.insert(0, "@.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, sticky="w")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.place(x=212, y=245)

add_button = Button(text="Add", width=31, command=save)
add_button.place(x=96, y=272)

search_button = Button(text="          Lookup          ", command=find_password)
search_button.place(x=212, y=200)

window.mainloop()
