import tkinter
from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack(side = "left")
my_label.config(text="Another New Text")
#my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=2, row=2)

window.mainloop()