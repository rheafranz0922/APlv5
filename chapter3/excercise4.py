import tkinter as tk
from tkinter import ttk, messagebox

def draw_shape():
    try:
        # Get the selected shape and coordinate values from the user
        selected_shape = shape_selection.get()
        coordinates = coordinate_entry.get()

        # Split the coordinates into a list of integers
        coordinates_list = [int(coord.strip()) for coord in coordinates.split(',')]

        # Dselected shape in a canvas
        if selected_shape == "Heart":
            canvas.create_heart(coordinates_list, outline="black")
        elif selected_shape == "Rectangle":
            canvas.create_rectangle(coordinates_list, outline="black")
        elif selected_shape == "circle":
            side_length = abs(coordinates_list[2] - coordinates_list[0])
            canvas.create_rectangle(coordinates_list, outline="pink")
        elif selected_shape == "Triangle":
            canvas.create_polygon(coordinates_list, outline="blue")
        else:
            messagebox.showerror("Error", "Please select a valid shape.")
            return

    except ValueError:
        messagebox.showerror("Error", "Please enter valid coordinates.")

# Create the main window
root = tk.Tk()
root.title("Draw Shape")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# shape selection
shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack()
shape_selection = ttk.Combobox(root, values=["Oval", "Rectangle", "Square", "Triangle"])
shape_selection.pack()

# Coordinate entry
coordinate_label = tk.Label(root, text="Enter Coordinates (comma-separated):")
coordinate_label.pack()
coordinate_entry = tk.Entry(root)
coordinate_entry.pack()

# Draw Button
draw_button = tk.Button(root, text="Draw  The Shape", command=draw_shape)
draw_button.pack(pady=10)

# Start the main event loop
root.mainloop()
