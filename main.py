from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import PyInstaller

FONT = ("Courier", 10, "bold")
# ---------------------------- SEARCH MACHINE------------------------------- #

def search():
    try:
        with open("data.json", "r") as data_file:
            search_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops..", message="You are not saved any password")
    searching_site = inp_web.get()
    if searching_site != "":
        try:
            needed_site = search_data[searching_site]
        except KeyError:
            messagebox.showinfo(title="Oops..", message="There are no password for this site")
        else:
            search_email = needed_site["email"]
            search_pass = needed_site["password"]
            messagebox.showinfo(title=searching_site, message=f"Email: {search_email} \n"
                                                f"Password: {search_pass}")
    else:
         messagebox.showinfo(title="Oops..", message="Please enter a website name")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)
    
    gen_password = "".join(password_list)
    inp_pass.delete(0, END)
    inp_pass.insert(0, gen_password)
    try:
        pyperclip.copy(gen_password)
    except:
        pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_save():
    web_data = inp_web.get()
    email_data = inp_eu.get()
    pass_data = inp_pass.get()
    new_data = {
        web_data: {
            "email": email_data,
            "password": pass_data,
        }
    }

    if web_data != "" or email_data != "" or pass_data != "":
        is_ok = messagebox.askokcancel(title=web_data,
                                       message=f"These are the details entered: \nEmail: {email_data} \n"
                                               f"Password: {pass_data}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    j_data = json.load(data)
                    j_data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                 with open("data.json", "w") as data:   
                    json.dump(j_data, data, indent=4)
            finally:
                inp_eu.delete(0, 'end')
                inp_web.delete(0, 'end')
                inp_pass.delete(0, 'end')
    else:
        messagebox.showinfo(title="Oops..", message="Please don't leave any fields empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password manager")
# ---------------------------- Canvas ------------------------------- #
canvas = Canvas()
canvas.config(width=200, height=190)
image_lock = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image_lock)
canvas.grid(column=1, row=0)
# ---------------------------- Texts ------------------------------- #
web = Label(text="Website:")
web.grid(column=0, row=1)
em_user = Label(text="Email/Username:")
em_user.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)
# ---------------------------- Inputs------------------------------- #
inp_web = Entry(width=32)
inp_web.grid(column=1, row=1)
inp_web.focus()
inp_eu = Entry(width=42)
inp_eu.grid(column=1, row=2, columnspan=2)
inp_pass = Entry(width=32)
inp_pass.grid(column=1, row=3)
# ---------------------------- Buttons------------------------------- #
add = Button(text="Add", width=36, command=password_save)
add.grid(column=1, row=4, columnspan=2)
generate = Button(text="Generate", command=passgen)
generate.grid(column=2, row=3)
search = Button(text="Search", width=7, command=search)
search.grid(column=2, row=1)
window.mainloop()