# =========================================
# Topic : Layout Managers
# =========================================

from tkinter import *

root = Tk()

root.geometry("500x400")

# =========================================
# pack()
# =========================================

Label(

    root,

    text="PACK",

    bg="red"

).pack()

# =========================================
# grid()
# =========================================

Label(

    root,

    text="Username"

).grid(row=0, column=0)

Entry(root).grid(row=0, column=1)

Label(

    root,

    text="Password"

).grid(row=1, column=0)

Entry(root).grid(row=1, column=1)

# =========================================
# place()
# =========================================

Button(

    root,

    text="Login"

).place(x=200, y=100)

root.mainloop()