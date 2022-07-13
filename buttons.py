from tkinter import *
from tkinter import Tk
def onclick(i):
    print(f"this button is for {i}")

def stats():
    buttons =[]
    win=Tk()
    win.title="buttons"
    for i in range(5):
        b =Button(win,height=10,width=100,command = lambda i = i :onclick(i))
        b.pack()
        buttons.append(b)
    win.mainloop()
    print(buttons)
stats()