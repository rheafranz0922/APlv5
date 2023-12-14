import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("300x150")

        self.create_widgets()

    def create_widgets(name):
        # Username Label and Entry
        tk.Label(name, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        name.username_entry = tk.Entry(name)
        name.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Password  use Label and Entry
        tk.Label(tk, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        tk.password_entry = tk.Entry(tk, show="*")
        tk.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Login Button
        login_button = tk.Button(tk, text="Login", command=tk.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        # Retrieve the entered username and password
        name = self.username_entry.get()
        password = self.password_entry.get()

        # Simple login validation (for demonstration purposes)
        if name == "user" and password == "pass":
            messagebox.showinfo("Login Successful", "Welcome, {}".format(name))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

app = LoginPage()
app.mainloop()

