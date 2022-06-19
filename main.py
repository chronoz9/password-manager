from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGen
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass_entry.delete(0, END)
    gen = PasswordGen()
    rand_pass = gen.generate_pass()
    pass_entry.insert(0, rand_pass)
    pyperclip.copy(rand_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    web = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if not web:
        messagebox.showerror('Empty Website', 'Please fill the website')
    elif not password:
        messagebox.showerror('Empty Password', 'Please fill the password')
    else:
        with open('pass_file.txt', 'a') as file:
            line = f"{web}|{email}|{password}\n"
            file.write(line)

        web_entry.delete(0, END)
        pass_entry.delete(0, END)

        messagebox.showinfo('Password Saved!', 'Your password has been added')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Safe Pass')
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)

picture = PhotoImage(file='logo.png')
canvas.create_image(100, 98, image=picture)
canvas.grid(column=1,row=0)

web_label = Label(text='Website')
web_label.grid(row=1, column=0)

user_label = Label(text='Email/Username')
user_label.grid(row=2, column=0)

pass_label = Label(text='Password')
pass_label.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'putugenin@gmail.com')

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_btn = Button(text='Generate Password', command=generate_pass)
generate_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=35, )
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
