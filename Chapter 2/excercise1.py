import tkinter as tk
from tkinter import Label, StringVar

# Create main window
root = tk.Tk()

change_font=('Arial', '14', 'bold')
# Configure window
root.title("The gui")
root.geometry("400x400") 
root.resizable(False, False)
root.configure(bg='#800080')

# Create widgets
message = "Welcome to the Excercise 1 Program!"
label_var = StringVar(value=message)

label = Label(root, textvariable=label_var, font=('Helvetica', '16', 'normal'), bg='#e6e6e6')
label.pack(pady=30)

font_button = tk.Button(root, text="Change Font Style", command=change_font)
font_button.pack()

root.mainloop()
