from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password_func():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letters_list = [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    symbols_list = [password_list.append(choice(symbols)) for char in range(randint(2, 4))]
    numbers_list = [password_list.append(choice(numbers)) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_g = website_entry.get()
    password_g = password_entry.get()
    email_g = email_entry.get()
    new_data = {
        website_g:{
        "email": email_g,
        "password": password_g,
        }
    }
    if len(website_g) == 0 or len(password_g) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("TKinter/27-Password Generator/data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("TKinter/27-Password Generator/data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("TKinter/27-Password Generator/data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_g = website_entry.get()
    try:
        with open("TKinter/27-Password Generator/data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Not Found", message="No data file found.")
    else:
        if website_g in data:
            email = data[website_g]['email']
            password = data[website_g]['password']
            messagebox.showinfo(title=website_g, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Not Found", message=f"No details for {website_g} found.")
    



# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="TKinter/27-Password Generator/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0,row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1,row=1)
website_entry.focus()

search = Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1)

email = Label(text="Email/Username:")
email.grid(column=0,row=2)

email_entry = Entry(width=52)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "samuilacamelia@gmail.com")

password = Label(text="Password:")
password.grid(column=0,row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)

generate_password = Button(text="Generate Password", command=generate_password_func)
generate_password.grid(column=2,row=3)

add = Button(text="Add", width=44, command=save)
add.grid(column=1,row=4,columnspan=2)






window.mainloop()