import tkinter as tk
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Title!")
window.geometry("600x300")

dogimg= PhotoImage(file="dog.png")

bsearch = Button(window,text="Search by name")
esearch = Entry(window,text="      ")
dog = Label(window, image="dogimg")
l1 = Label(window,text="Client Database")
lname = Label(window,text="Name")
ltype = Label(window,text="Type")
lbreed = Label(window,text="Breed")
lowner = Label(window,text="Owner")
lbday = Label(window,text="Birthdate")
ename = Entry(window,text="       ")
etype = Entry(window,text="       ")
ebreed = Entry(window,text="       ")
eowner = Entry(window,text="       ")
ebday = Entry(window,text="       ")
bprev = Button(window,text="< Previous")
bsave = Button(window,text="Save Entry")
bnext = Button(window,text="Next >")


dog.pack()

window.mainloop()