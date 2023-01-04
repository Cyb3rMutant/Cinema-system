#Adapted from source = https://www.pythontutorial.net/tkinter/tkinter-options/

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
ttk.Label(root, text='Hi, there').pack()


yourlabel = ttk.Label(root)
yourlabel['text'] = 'Hi, there, I am here'
yourlabel.pack()


mylabel = ttk.Label(root)
mylabel.config(text='Hi, there, I heading home!')
mylabel.pack()

root.mainloop()
