import tkinter as tk

root = tk.Tk()
bgc = "#22263D"

left_frame = tk.Frame(root, bd=5)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(root, bd=5) 
right_frame.pack(side="right", fill="both", expand=True)

label_a = tk.Label(left_frame, text="A", bg=bgc, padx=40, pady=20)
label_a.pack(side="top", fill="both", expand=True) 

label_b = tk.Label(left_frame, text="B", padx=40, pady=20)
label_b.pack(side="bottom", fill="both", expand=True)

label_c = tk.Label(right_frame, text="C", padx=40, pady=20)
label_c.pack(side="top", fill="both", expand=True)

label_d = tk.Label(right_frame, text="D", bg=bgc, padx=40, pady=20)
label_d.pack(side="bottom", fill="both", expand=True)

root.mainloop()