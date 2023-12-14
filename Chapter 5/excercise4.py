import tkinter as tk
from math import pi

class Shape:
    def __init__(self):
        self.sides = []

    def input_sides(self):
        pass

    def area(self):
        pass
#Define the shapes.
class Circle(Shape):
    def input_sides(self):
        radius = float(input("Enter the radius of the circle: "))
        self.sides = [radius]

    def area(entry):
        radius = entry.sides[0]
        return pi * radius**2
# Define a class for a square.
class Square(Shape):
    def input_sides(self):
        side = float(input("Enter the side length of the square: "))
        self.sides = [side]

    def area(self):
        side = self.sides[0]
        return side ** 2
# Define a class of triangle.
class Triangle(Shape):
    def input_sides(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.sides = [base, height]

    def area(self):
        base, height = self.sides
        return 0.5 * base * height
# Define a Tkinter GUI class
class ShapeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(label):
        tk.Label(label, text="Select a Shape:").pack()

        shape_var = tk.StringVar()
        shape_var.set("Circle")

        shape_option_menu = tk.OptionMenu(label, shape_var, "Circle", "Square", "Triangle")
        shape_option_menu.pack()

        tk.Button(label, text="Calculate Area", command=lambda: label.calculate_area(shape_var.get())).pack()

    def calculate_area(self, selected_shape):
        if selected_shape == "Circle":
            shape = Circle()
        elif selected_shape == "Square":
            shape = Square()
        elif selected_shape == "Triangle":
            shape = Triangle()
        else:
            return

        shape.input_sides()
        area_result = shape.area()

        result_label = tk.Label(self, text=f"Area of {selected_shape}: {area_result}")
        result_label.pack()
#The final.
app = ShapeGUI()
app.mainloop()