# =========================================
# Topic : Entry Widget
# =========================================

from tkinter import *

root = Tk()

root.geometry("400x300")

# Function
def show():

    print(entry.get())

# Entry box
entry = Entry(

    root,

    font=("Arial", 20)

)

entry.pack(pady=20)

# Button
btn = Button(

    root,

    text="Submit",

    command=show
)

btn.pack()

root.mainloop()