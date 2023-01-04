#https://www.pythontutorial.net/tkinter/tkinter-command/

import tkinter as tk
from tkinter import ttk

def my_event(event):
    print('The process event function was called')
    
#1. Trying simple event biding
root = tk.Tk()
my_btn = ttk.Button(root, text='Example')
my_btn.bind("<Enter>", my_event)
#my_btn.focus()
my_btn.pack(expand=True)

#2. Trying to demonstrate binding of multiple handlers for the same event
def log(event):
    print(event)

myroot = tk.Tk()
myroot.geometry('300x200+500+100') 

btn = ttk.Button(myroot, text='Save')
btn.bind('<Enter>', my_event)
btn.bind('<Enter>', log, add='+')

btn.focus()
btn.pack(expand=True)

#3. Testing whether two windows can be displayed .. 
root.mainloop()
myroot.mainloop()