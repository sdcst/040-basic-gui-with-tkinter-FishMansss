import tkinter as tk
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Title!")
window.geometry("400x70")

e1 = Entry(window,text="          ")
l1 = Label(window,text="x")
e2 = Entry(window,text="          ")
l2 = Label(window,text="=")
a1 = Entry(window,text="          ")


e1.pack(side=LEFT)
l1.pack(side=LEFT)
e2.pack(side=LEFT)
l2.pack(side=LEFT)
a1.pack(side=LEFT)
window.mainloop()