import tkinter as tk
from tkinter import ttk, messagebox

#I use the code from a function about the shape.
def calculate_area():
    try:
        #THis the selected the shape of a circle, square, and rectangle.
        if selected_shape.get() == "Circle":
            radius = float(radius_entry.get())
            area = 3.14 * radius**2
        elif selected_shape.get() == "Square":
            side_length = float(side_length_entry.get())
            area = side_length**2
        elif selected_shape.get() == "Rectangle":
            length = float(length_entry.get())
            width = float(width_entry.get())
            area = length * width
        else: #Display the error.
            messagebox.showerror("Error", "Please select a valid shape.")
            return
    #To update the result.
        result_label.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid dimensions.")

#Main root
root = tk.Tk()
root.title("Area Calculator")

#To create to interface the tab
tab_control = ttk.Notebook(root)

# Create tabs for Circle, Square, and Rectangle.
circle_tab = ttk.Frame(tab_control)
square_tab = ttk.Frame(tab_control)
rectangle_tab = ttk.Frame(tab_control)

tab_control.add(circle_tab, text="Circle")
tab_control.add(square_tab, text="Square")
tab_control.add(rectangle_tab, text="Rectangle")

tab_control.pack(expand=1, fill="both")

#Create a selection for the shapes.
selected_shape = tk.StringVar(value="Circle")
shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack()
shape_selection = ttk.Combobox(root, textvariable=selected_shape, values=["Circle", "Square", "Rectangle"])
shape_selection.pack()


#The circle
radius_label = tk.Label(circle_tab, text="Enter Radius:")
radius_label.pack(pady=10)
radius_entry = tk.Entry(circle_tab)
radius_entry.pack(pady=10)

#Square
side_length_label = tk.Label(square_tab, text="Enter Side Length:")
side_length_label.pack(pady=10)
side_length_entry = tk.Entry(square_tab)
side_length_entry.pack(pady=10)

#rectangle
length_label = tk.Label(rectangle_tab, text="Enter Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(rectangle_tab)
length_entry.pack(pady=10)

width_label = tk.Label(rectangle_tab, text="Enter the Width:")
width_label.pack(pady=10)
width_entry = tk.Entry(rectangle_tab)
width_entry.pack(pady=10)

#result label
result_label = tk.Label(root, text="Area: ")
result_label.pack(pady=10)

#The button for calculate
calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack(pady=10)

#the result of my output
root.mainloop()