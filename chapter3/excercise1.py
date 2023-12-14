# Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

#In InputFrame, include the following:

# A title label in blue.
#An entry field for the user's name.
#A dropdown menu for selecting a color.
#An "Update Greeting" button.
#In DisplayFrame, include a label to display the personalized greeting.
#Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.
#Use different background colors for each frame.
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Greeting app")
root.geometry("400x400")

#Create Background color of a frame
frame = tk.Frame(root, bg="lightpink")
frame.pack(expand=True, fill="both")

headinglabel = tk.Label(root, text='Hi, What is your name?', fg='blue')
headinglabel.pack()

name = tk.Entry(root)
name.pack()

def on_click():
    selected_color = color_chosen.get()
    username = name.get()


    result = tk.Label(root,text=f"Hi {username},your favorite color is{selected_color}",fg=selected_color)
    result.pack()

# Dropdown list options
dropdown_list = ["blue", "purple", "red"]

colorlabel = tk.Label(root, text="Select the color")
colorlabel.pack()
# Create a Combobox
color_chosen = ttk.Combobox(root, values=dropdown_list)
color_chosen.pack()
#Button
button_label = tk.Button(root, text="Update Greeting",command=on_click, padx=50)
button_label.pack(pady=50)
root.mainloop()