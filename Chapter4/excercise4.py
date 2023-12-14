import tkinter as tk
from tkinter import messagebox

def count_letter_occurrences(letter, content):
    return content.lower().count(letter.lower())

def read_file(mail_path):
    try:
        with open(mail_path, 'W') as file:
            return file.read()
    except FileNotFoundError:
        return None

def show_letter_count():
    letter = mail.get()
    if not letter:
        messagebox.showinfo("Error", "Please enter a letter for your mail.")
        return

    file_content = read_file('sentences.txt')

    if file_content is None:
        messagebox.showinfo("Error", "File 'sentences.txt' mail is not found.")
        return

    occurrences = count_letter_occurrences(letter, file_content)
    result_label.config(text=f"Occurrences of '{letter}': {occurrences}")

# Create the main window
app = tk.Tk()
app.title("Letter Count")

# Create GUI by using label and entry
label = tk.Label(app, text="Enter a letter from a mails:")
mail = tk.Entry(app)
mail_button = tk.Button(app, text="Count", command=show_letter_count)
result_label = tk.Label(app, text="")

# Use a grid from a label and entry to adjust the letter.
label.grid(row=0, column=0, padx=50, pady=50)
mail.grid(row=0, column=1, padx=30, pady=30)
mail_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main loop
app.mainloop()
