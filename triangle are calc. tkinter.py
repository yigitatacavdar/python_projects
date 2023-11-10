#a lot to learn.
from tkinter import *

window = Tk()
window.title("Triangle Are Calculator")
window.geometry("360x360")

lbl1 = Label(window, text="TRIANGLE AREA CALCULATOR", font=("ariel bold", 10))
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Enter the height of the triangle:")
lbl2.grid(column=0, row=1)

lbl3 = Label(window, text="Enter the base of the triangle:   ")
lbl3.grid(column=0, row=2)

lbl = Label(window, text="")

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=1)

txt2 = Entry(window, width=10)
txt2.grid(column=1, row=2)

def clicked():

    x = txt1.get()
    y = txt2.get()

    a = int(x)
    b = int(y)

    res = (a * b)/ 2
    
    lbl.configure(text = res)
    lbl.grid(column=1, row=4)

btn = Button(window, text = "Calculate!", command = clicked)
btn.grid(column=1, row=3)

window.mainloop()