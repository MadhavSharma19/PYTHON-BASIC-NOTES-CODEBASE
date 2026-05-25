# =========================================
# Topic : Checkbox Widget
# =========================================

from tkinter import *

root = Tk()

root.geometry("400x300")

# Variable
python_var = IntVar()

java_var = IntVar()

# Function
def show():

    print("Python =", python_var.get())

    print("Java =", java_var.get())

# Checkboxes
Checkbutton(

    root,

    text="Python",

    variable=python_var

).pack()

Checkbutton(

    root,

    text="Java",

    variable=java_var

).pack()

Button(

    root,

    text="Submit",

    command=show

).pack()

root.mainloop()