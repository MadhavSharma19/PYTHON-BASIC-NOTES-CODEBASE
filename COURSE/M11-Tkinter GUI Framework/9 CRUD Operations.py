# =========================================
# Topic : CRUD Operations
# =========================================

# CRUD:
# Create
# Read
# Update
# Delete

from tkinter import *

root = Tk()

root.geometry("500x500")

students = []

# =========================================
# Add Data
# =========================================

def add():

    students.append(entry.get())

    listbox.insert(END, entry.get())

    entry.delete(0, END)

# =========================================
# Delete Data
# =========================================

def delete():

    selected = listbox.curselection()

    listbox.delete(selected)

# =========================================
# Update Data
# =========================================

def update():

    selected = listbox.curselection()

    listbox.delete(selected)

    listbox.insert(selected, entry.get())

# =========================================
# Read Data
# =========================================

def show():

    print(students)

# Entry
entry = Entry(

    root,

    font=("Arial", 20)

)

entry.pack()

# Listbox
listbox = Listbox(

    root,

    font=("Arial", 20),

    width=20,

    height=10
)

listbox.pack()

# Buttons
Button(root, text="Add", command=add).pack(fill=BOTH)

Button(root, text="Delete", command=delete).pack(fill=BOTH)

Button(root, text="Update", command=update).pack(fill=BOTH)

Button(root, text="Show", command=show).pack(fill=BOTH)

root.mainloop()