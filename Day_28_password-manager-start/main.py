from tkinter import *
from tkinter import messagebox
import pyperclip
from password_gernater import GarnetPassword
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerent_password() :
    password = GarnetPassword.password_generator()
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_recode():
    f = open("text_file.txt", "a")
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()


    is_ok = messagebox.askokcancel(title="Website", message="Do you want to save this website: {website} | email: {email} | password: {password}\n")
    if is_ok:
        f.write(f"website: {website} | email: {email} | password: {password}\n")
        messagebox.showinfo(title="Save", message="Password saved successfully")
        website_input.delete(0,END)
        email_input.delete(0,END)
        password_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=60, pady=60)
window.minsize(width=200, height=200)
canvas = Canvas(width=200, height=200)

icon = PhotoImage(file="Day_28_password-manager-start/logo.png")  # Replace with the path to your icon file
window.iconphoto(False, icon)

img = PhotoImage(file="Day_28_password-manager-start/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1,columnspan=2)
website_input.focus()

email_label = Label(text="email/username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2,columnspan=2)
email_input.insert(0, "test@gmail.com")

password_label = Label(text="password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

grant_password_button = Button(text="Generate Password",command=gerent_password)
grant_password_button.grid(column=2, row=3)

add_button = Button(text="Add",command=add_recode, width=36)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()