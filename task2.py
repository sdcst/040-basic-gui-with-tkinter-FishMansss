import tkinter as tk
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("630x170")

#window.configure(background='white')
dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto, borderwidth=3)

bsearch = Button(window,text="Search by name")
esearch = Entry(window,text="      ")

l1 = Label(window,text="Client Database")
lname = Label(window,text="    Name    ")
ltype = Label(window,text="    Type    ")
lbreed = Label(window,text="   Breed   ")
lowner = Label(window,text="   Owner   ")
lbday = Label(window,text="  Birthdate  ")
ename = Entry(window,text="       ")
etype = Entry(window,text="       ")
ebreed = Entry(window,text="       ")
eowner = Entry(window,text="       ")
ebday = Entry(window,text="       ")
bprev = Button(window,text="< Previous")
bsave = Button(window,text="Save Entry")
bnext = Button(window,text="Next >")

#grid pack
dog.grid(row=1, column = 1, rowspan = 2)
bsearch.grid(row=1, column=4)
esearch.grid(row=1, column=5)
l1.grid(row=1, column=3, rowspan=2)
lname.grid(row=4, column=1)
ltype.grid(row=4, column=2)
lbreed.grid(row=4, column=3)
lowner.grid(row=4, column=4)
lbday.grid(row=4, column=5)

ename.grid(row=5, column=1)
etype.grid(row=5, column=2)
ebreed.grid(row=5, column=3)
eowner.grid(row=5, column=4)
ebday.grid(row=5, column=5)

bprev.grid(row=6,column=1)
bsave.grid(row=6,column=3)
bnext.grid(row=6,column=5)
window.mainloop()