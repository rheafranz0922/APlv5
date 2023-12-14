import tkinter as tk
from tkinter import messagebox

#Create window root.
root = tk.Tk()
root.title("Coffee Machine")

#The option or the menu of a coffee.
coffee_options = ["Cappuccino", "Mocha", "Espresso"]
coffee_var =tk.StringVar(root)
coffee_var.set(coffee_options[0])

#Creating the dropdown.
coffee_dropdown = tk.OptionMenu(root, coffee_var, *coffee_options)
coffee_dropdown.pack()

milk_var = tk.IntVar(value=0)
milk_checkbox = tk.Checkbutton(root, text="Add Milk", variable=milk_var)
milk_checkbox.pack()

def order():
    coffee = coffee_var.get()
    has_milk = "with milk" if milk_var.get() == 1 else ""
    messagebox.showinfo("Order", f"You ordered: {coffee} {has_milk}")

order_button = tk.Button(root, text="Order Coffee", comand=order)
order_button.pack()

root.mainloop()