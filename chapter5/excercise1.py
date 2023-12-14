import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(dog, name, age, breed):
        dog.name = name
        dog.age = age
        dog.breed = breed

    def woof(dog):
        return f"{dog.name} says: Woof! Woof!"

# I use the Function for the dog to create instances and display information
def display_dog_info():
    # Dog 1
    dog1 = Dog("Lukie", 1, "Saluki")
    info_text1 = f"Dog 1 Information:\nName: {dog1.name}\nAge: {dog1.age}\nBreed: {dog1.breed}\n\n"

    # Dog 2
    dog2 = Dog("Chloe", 5, "poodle")
    info_text2 = f"Dog 2 Information:\nName: {dog2.name}\nAge: {dog2.age}\nBreed: {dog2.breed}\n"

    #Dog 3
    dog3 = Dog("Nooroo", 3, "Husky")
    info_text3 = f"Dog 3 information:\nName: {dog3.name}\nAge: {dog3.age}\nBreed: {dog3.breed}"

    messagebox.showinfo("Dog Information", info_text1 + info_text2)

if __name__ == "__main__":
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Dog Information")

    # Button to display dog information
    display_button = tk.Button(root, text="Dog-Info", command=display_dog_info)
    display_button.pack(pady=20)

    # Start the Tkinter event loop
    root.mainloop()
