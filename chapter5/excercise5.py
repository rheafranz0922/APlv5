import tkinter as tk

class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        self.type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

    def say_hello(self):
        return f"Hello, here is the member of an animals{self.name}!"

    def make_noise(self):
        return f"{self.name} says: {self.noise}"

class AnimalGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playing around in class")
        self.geometry("400x350")

        self.create_widgets()

    def create_widgets(self):
        self_type = tk.Label(self, text="Animal Type:")
        self_type.pack()
        entry_type = tk.Entry(self)
        entry_type.pack()

        self_name = tk.Label(self, text="Name:")
        self_name.pack()
        entry_name = tk.Entry(self)
        entry_name.pack()

        self_color = tk.Label(self, text="Color:")
        self_color.pack()
        entry_color = tk.Entry(self)
        entry_color.pack()

        self_age = tk.Label(self, text="Age:")
        self_age.pack()
        entry_age = tk.Entry(self)
        entry_age.pack()

        label_weight = tk.Label(self, text="Weight:")
        label_weight.pack()
        entry_weight = tk.Entry(self)
        entry_weight.pack()

        label_noise = tk.Label(self, text="Noise:")
        label_noise.pack()
        entry_noise = tk.Entry(self)
        entry_noise.pack()

        button_create = tk.Button(self, text="Create Animal", command=lambda: self.create_animal(entry_type.get(), entry_name.get(), entry_color.get(), entry_age.get(), entry_weight.get(), entry_noise.get()))
        button_create.pack()

    def create_animal(self, animal_type, name, color, age, weight, noise):
        animal = Animal(animal_type, name, color, age, weight, noise)

        # Display results in the console
        print(animal.say_hello())
        print(animal.make_noise())

app = AnimalGUI()
app.mainloop()

