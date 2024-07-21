from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.configure(padx=20,pady=20)

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609, 1)
    answer.config(text=f"{km}")
    
input = Entry()
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

text = Label(text="is equal to")
text.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate",command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
