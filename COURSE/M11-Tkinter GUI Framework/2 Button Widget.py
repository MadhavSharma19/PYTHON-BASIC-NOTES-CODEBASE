# =========================================
# Topic : Button Widget
# =========================================

from tkinter import *

root = Tk()

root.geometry("400x300")

root.title("Button Example")

# Function
def click():

    print("Button Clicked")

# Button
btn = Button(

    root,

    text="Click Me",

    font=("Arial", 20),

    bg="blue",

    fg="white",

    command=click
)

btn.pack(pady=50)

root.mainloop()