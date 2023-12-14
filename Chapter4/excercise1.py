import tkinter as tk

class UserInfoApp:
    def __init__(User, master):
        User.master = master
        User.master.title("User Information")

        # Create the widgets for user input
        tk.Label(master, text="Name:").pack()
        User.name_entry = tk.Entry(master)
        User.name_entry.pack()

        tk.Label(master, text="Age:").pack()
        tk.age_entry = tk.Entry(master)
        tk.age_entry.pack()

        tk.Label(master, text="Hometown:").pack()
        tk.hometown_entry = tk.Entry(master)
        tk.hometown_entry.pack()

        # Button is to click for user
        User.submit_button = tk.Button(master, text="Submit", command=User.write_and_read_info)
        User.submit_button.pack()

    def write_and_read_info(self):
        # Get user input values
        name = self.name_entry.get()
        age = self.age_entry.get()
        hometown = self.hometown_entry.get()

        # Write information of a file for user.
        with open("bio.txt", "w") as file:
            file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

        # Read and output user information from the file.
        with open("bio.txt", "r") as file:
            user_info = file.read()
            tk.messagebox.showinfo("User Information", user_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()
