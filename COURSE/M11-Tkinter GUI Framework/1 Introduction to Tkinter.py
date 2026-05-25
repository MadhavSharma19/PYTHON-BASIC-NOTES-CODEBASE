# =========================================
# Topic : Introduction to Tkinter
# =========================================

# Tkinter is used to create GUI applications

import tkinter as tk

# Creating window
app = tk.Tk()

# Window title
app.title("My First GUI")

# Window size
app.geometry("400x300")

# Label
label = tk.Label(
    app,
    text="Welcome to Tkinter",
    font=("Arial", 20)
)

label.pack(pady=50)

# Running window
app.mainloop()