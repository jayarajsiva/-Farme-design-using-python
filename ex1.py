from tkinter import *
from tkinter import messagebox

root = Tk()


root.title("Arithmetic Calculator")
root.geometry("350x300")
root.config(bg="#e6f2ff")


Label(root, text="Enter First Number:", bg="#e6f2ff", font=("Arial", 10, "bold")).pack(pady=5)
entry1 = Entry(root, width=25, font=("Arial", 10))
entry1.pack(pady=5)

Label(root, text="Enter Second Number:", bg="#e6f2ff", font=("Arial", 10, "bold")).pack(pady=5)
entry2 = Entry(root, width=25, font=("Arial", 10))
entry2.pack(pady=5)


def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showwarning("Warning", "Division by zero is not allowed!")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


frame = Frame(root, bg="#e6f2ff")
frame.pack(pady=10)

Button(frame, text="+", width=8, command=add, bg="#cce5ff", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
Button(frame, text="-", width=8, command=subtract, bg="#cce5ff", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
Button(frame, text="×", width=8, command=multiply, bg="#cce5ff", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
Button(frame, text="÷", width=8, command=divide, bg="#cce5ff", font=("Arial", 10, "bold")).grid(row=1, column=1, padx=5, pady=5)


result_label = Label(root, text="Result: ", bg="#e6f2ff", font=("Arial", 12, "bold"))
result_label.pack(pady=20)


root.mainloop()

