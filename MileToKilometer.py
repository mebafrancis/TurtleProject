import tkinter
from tkinter import *

def button_clicked():
    new_text = input.get()
    converted_text = float(new_text) * 1.60934
    km_result.config(text=converted_text)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Entry for miles
input = Entry(width=10)
input.grid(column=5, row=0)

#Label for miles
miles_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=7, row=0)

#Label for equal to
equal_label = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=3, row=1)

#Label for Km result
km_result = tkinter.Label(text="0", font=("Arial", 24, "bold"))
km_result.grid(column=5, row=1)

#Label for Km
km_label = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=7, row=1)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=5, row=2)

window.mainloop()