import tkinter

mile_calc = tkinter.Tk()
mile_calc.title("Mile to Km Converter")
mile_calc.minsize(width=500, height=500)
mile_calc.config(padx=20, pady=20)

input = tkinter.Entry(width=7)
input.grid(row=0, column=1)

my_label_1 = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
my_label_1.grid(row=0, column=2)

my_label_2 = tkinter.Label(text="is Equal to", font=("Arial", 24, "bold"))
my_label_2.grid(row=1, column=0)

my_label_3 = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
my_label_3.grid(row=1, column=2)

my_label_4 = tkinter.Label(text="0", font=("Arial", 24, "bold"))
my_label_4.grid(row=1, column=1)

def calculate():
    km_ans = float(input.get())*1.609
    round(km_ans)
    my_label_4["text"] = str(km_ans)


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)














mile_calc.mainloop()