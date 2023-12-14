import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create a window by using a root
root = tk.Tk()
root.title("Simple Calculator")

# Use the user input
entry = tk.Entry(root, width=16, font=("Arial", 18), bd=5, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4)

# Here is the button to click the number
buttons = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', 'C', '=', '+'
]

# Row and column indices for grid layout
row_val = 1
col_val = 0

# Create a button with a grid
for button in buttons:
    tk.Button(root, text=button, width=4, height=2,
              command=lambda b=button: on_button_click(b) if b != '=' else calculate() if b == '=' else clear_entry(),
              font=("Arial", 14)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
