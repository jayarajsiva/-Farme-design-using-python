from tkinter import *

root= Tk()
root.title("BCA APP")
root.geometry("500x700")
f1=Frame(root)
f1.config (bg="sky blue")
f1.pack(fill=BOTH,expand= True)
l1=Label(f1,text="ARITHEMATIC OPERATION",bg="brown",fg="yellow",font=("arial"," 15 ","bold"))
l1.pack()
f2=Frame(root)
f2.config(bg="pink")
f2.pack(fill=BOTH,expand=True)
l2=Label (f2,text="First number",fg="brown",bg="orange" ,font=("arial","10","bold"))
l2.pack()
root.mainloop()

