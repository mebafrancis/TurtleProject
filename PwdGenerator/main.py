from tkinter import *
import tkinter

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    open("data.txt", "a").write(f"{input.get()} | {input1.get()} | {input2.get()}\n")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=224, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = tkinter.Label(text="Website:  ", font=("Arial", 13, "bold"))
website_label.grid(column=0, row=1)

email_uname_label = tkinter.Label(text="Email/Username:  ", font=("Arial", 13, "bold"))
email_uname_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:  ", font=("Arial", 13, "bold"))
password_label.grid(column=0, row=3)

#Entry for website
input = Entry(width=35)
input.grid(column=1, row=1 , columnspan=2)
input.focus()

#Entry for email/username
input1 = Entry(width=35)
input1.grid(column=1, row=2 , columnspan=2)
input1.insert(0,"melbahere@gmail.com")

#Entry for password
input2 = Entry(width=35)
input2.grid(column=1, row=3,columnspan=2)

#Button
button = Button(text="Generate Password")
button.grid(column=2, row=3)

#Button
button1 = Button(text="Add", width=35,command=save)
button1.grid(column=1, row=4, columnspan= 2 )

window.mainloop()
