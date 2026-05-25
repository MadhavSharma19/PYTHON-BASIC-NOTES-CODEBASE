# =========================================
# Topic : Radio Button
# =========================================

from tkinter import *

root = Tk()

root.geometry("400x300")

# Variable
gender = StringVar()

# Function
def show():

    print("Selected =", gender.get())

# Radio buttons
Radiobutton(

    root,

    text="Male",

    variable=gender,

    value="Male"

).pack()

Radiobutton(

    root,

    text="Female",

    variable=gender,

    value="Female"

).pack()

Button(

    root,

    text="Submit",

    command=show

).pack()

root.mainloop()