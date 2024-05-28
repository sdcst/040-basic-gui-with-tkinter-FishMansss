import tkinter 
from tkinter import *
from tkinter import ttk

#
window = Tk()
window.title("Example")
window.geometry("250x135")

#Labels
dogphoto = PhotoImage(file="dog.png")
dogimg = Label(window, image=dogphoto, borderwidth=3, relief=SUNKEN)
lname = Label(window, text="Pochacco!")
text = Label(window, text=" A cuddly little puppy! This is from the same\ncreators who brough you keropi and kero kero", background="cyan")

#Placing
dogimg.grid(row=1,column=1)
lname.place(x=160,y=50)
text.grid(row=3,column=1)


window.mainloop()