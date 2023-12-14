import tkinter as tk
root = tk.Tk()


root.title("Resizable GUI with Labels")


# Create labels with text
label1 = tk.Label(root, text="A", padx=20, bg="red")
label2 = tk.Label(root, text="B", padx=20, bg="yellow")
label3 = tk.Label(root, text="C", padx=20, bg="blue")
label4 = tk.Label(root, text="D", padx=20, bg="white")

# Pack labels with specified geometry
label1.pack(side="top",fill=tk.X, expand=True)
label2.pack(side="bottom")
label3.pack(side="left", fill=tk.Y, expand=True)
label4.pack(side="right")

root.mainloop()

