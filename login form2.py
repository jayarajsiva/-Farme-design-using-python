from tkinter import *

root = Tk()
root.title("student mark list")
root.geometry ("500x400")
l= Label (root,text="user Name ")
l.pack()
e=Entry(root)
e.pack()
b = Button(root,text="Login")
b.pack()
root.mainloop()
