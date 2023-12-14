import tkinter as tk
from tkinter import messagebox
import re

def is_valid_password(password):
    # Pick a password code.
    if (6 <= len(password) <= 12 and
            re.search("[a-z]", password) and
            re.search("[0-9]", password) and
            re.search("[A-Z]", password) and
            re.search("[$#@]", password)):
        return True
    return False

def check_password():
    password = password.get()

    if is_valid_password(password):
        messagebox.showinfo("Password Valid", "Password is valid!")
    else:
        messagebox.showwarning("Invalid Password", "Password is not workin please try again!")

# Create thhe window
app = tk.Tk()
app.title("Password Check")

# Creating the gui from a password
password = tk.Label(app, text="Enter password:")
password = tk.Entry(app, show="*")  # Show asterisks for password entry
check_button = tk.Button(app, text="Please my check password", command=check_password)

# Place components on the window
password.pack(pady=10)
password.pack(pady=10)
check_button.pack(pady=10)

# Result of a  main loop
app.mainloop()
