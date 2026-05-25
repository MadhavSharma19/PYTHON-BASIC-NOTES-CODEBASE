# =========================================
# Topic : Canvas Widget
# =========================================

from tkinter import *

root = Tk()

root.geometry("500x400")

# Canvas
c = Canvas(

    root,

    width=400,

    height=300,

    bg="black"
)

c.pack()

# Drawing shapes
c.create_rectangle(50, 50, 200, 150, fill="blue")

c.create_oval(220, 50, 350, 180, fill="red")

c.create_line(0, 0, 400, 300, fill="white", width=5)

root.mainloop()