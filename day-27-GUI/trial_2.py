import tkinter
# from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)             # Adding moe space around program
# frame = tkinter.Frame(window)
# frame.pack

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="top")
my_label.grid(column=0, row=0)

# my_label["text"] = "New Text"           # Change labels by using one of these methods
# my_label.config(text="New Text")

#Button

def button_clicked():
    my_label.config(text=input.get())
    # print(input.get())
    # print("i got clicked")

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# Input
input = tkinter.Entry(width=20)
input.grid(column=3, row=2)

button_2 = tkinter.Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

window.mainloop()