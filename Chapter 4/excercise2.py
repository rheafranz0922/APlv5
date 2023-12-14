import tkinter as tk

class input:
    def __init__(self, master):
        self.master = master
        self.master.title("User Information")

        # Create Entry widgets for user input
        tk.Label(master, text="Name:").pack()
        input.name_entry = tk.Entry(master)
        input.name_entry.pack()

        tk.Label(master, text="Age:").pack()
        input.age_entry = tk.Entry(master)
        input.age_entry.pack()

        tk.Label(master, text="Hometown:").pack()
        self.hometown_entry = tk.Entry(master)
        self.hometown_entry.pack()

        # Button to write and read user information
        self.submit_button = tk.Button(master, text="Submit", command=self.write_and_read_info)
        self.submit_button.pack()

    def write_and_read_info(self):
        # Get user input values
        name = self.name_entry.get()
        age = self.age_entry.get()
        hometown = self.hometown_entry.get()

        # Write user information of a file
        with open("bio.txt", "w") as file:
            file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

        # Read and output user information from the file
        with open("bio.txt", "r") as file:
            user_info = file.read()
            tk.messagebox.showinfo("User Information", user_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = input(root)
    root.mainloop()
