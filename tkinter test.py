from tkinter import *

window = Tk()
window.title("App")
window.geometry('350x200')

lbl = Label(window, text="Enter your name:")
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():
    
    res = "Welcome, " + txt.get() + "!"
    lbl.configure(text = res)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()