#Source: https://www.pythontutorial.net/tkinter/tkinter-pack/

import tkinter as tk
from tkinter import ttk

def login():
    print("User name : " + username.get() + "\nPassword : " + password.get())

root = tk.Tk()
root.title('Login')
root.geometry("350x220")

username = tk.StringVar()
password = tk.StringVar()

fields = {} # dictionary

fields['username_label'] = ttk.Label(text='Username:')
fields['username'] = ttk.Entry(textvariable=username)

fields['password_label'] = ttk.Label(text='Password:')
fields['password'] = ttk.Entry(textvariable=password, show="*")

for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Login', command=login).pack(anchor=tk.W, padx=10, pady=5)

root.mainloop()