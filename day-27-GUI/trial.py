from tkinter import *
import tkinter


calc_window = tkinter.Tk()
calc_window.title('Calculator Program')
frame = Frame(calc_window)
frame.pack()


button_1 = tkinter.Button(frame,text = 'My First Program', width ='20', height = '20')
button_1.pack(side=LEFT)


calc_window.mainloop()