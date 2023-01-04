#Source: https://www.pythontutorial.net/tkinter/tkinter-place/
import tkinter as tk

root = tk.Tk()
root.title('Place Geometry Manager - Example')

label1 = tk.Label(root, text="Absolute values", bg='blue', fg='white').place(x=20, y=10)
label2 = tk.Label(root, text="Relative value", bg='green', fg='white').place(relx=0.8, rely=0.8, relwidth=0.5, relheight=0.5, anchor='se')

root.mainloop()