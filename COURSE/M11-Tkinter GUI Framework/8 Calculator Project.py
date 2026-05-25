# =========================================
# Topic : Calculator Project
# =========================================

from tkinter import *

root = Tk()

root.geometry("350x400")

root.title("Calculator")

# Entry box
e = Entry(

    root,

    font=("Arial", 25),

    bd=10

)

e.pack(fill=BOTH)

# Function
def click(num):

    e.insert(END, num)

# Clear function
def clear():

    e.delete(0, END)

# Calculate function
def equal():

    result = eval(e.get())

    e.delete(0, END)

    e.insert(0, result)

# Buttons
Button(root, text="1", command=lambda: click(1)).pack(fill=BOTH)

Button(root, text="2", command=lambda: click(2)).pack(fill=BOTH)

Button(root, text="3", command=lambda: click(3)).pack(fill=BOTH)

Button(root, text="+", command=lambda: click("+")).pack(fill=BOTH)

Button(root, text="=", command=equal).pack(fill=BOTH)

Button(root, text="Clear", command=clear).pack(fill=BOTH)

root.mainloop()