#Source: https://www.pythontutorial.net/tkinter/tkinter-pack/
#Source: https://www.pythontutorial.net/tkinter/tkinter-grid/

import tkinter as tk
from tkinter import ttk

def login():
    print("User name : " + username.get() + "\nPassword : " + password.get())

root = tk.Tk()
root.title('Login')
root.geometry("250x120")
root.resizable(0,0)

root.columnconfigure(0, weight=1)   #1st column width is 1
root.columnconfigure(1, weight=3)   #2nd columns is almost 3 times width to 1st column

username = tk.StringVar()
password = tk.StringVar()

username_label = ttk.Label(root,text='Username:').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
username_entry = ttk.Entry(root, textvariable=username).grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

password_label = ttk.Label(root, text='Password:').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
password_entry = ttk.Entry(root, textvariable=password, show="*").grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

login_button = ttk.Button(root, text='Login', command=login).grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()