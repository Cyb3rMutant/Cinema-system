# Source: https://www.pythontutorial.net/tkinter/tkinter-hello-world/ 
# Source: https://www.pythontutorial.net/tkinter/tkinter-ttk/

# ttk are TK themed widgets. These were introduced in 2007 with TK8.5
# and replace many but not all TK classic widgets.

# tkinter.ttk module contains all ttk widgets and where possible we
# should use ttk widgets as it helps app to automatically adopt native
# look and feel of the platform on which application runs and ttk lets
# separate the code that implements the behaviour from their appearance 
# through styling system.

# Some new ttk widgets e.g., Progeressbar, Treeview, Separator, etc. 
# See more at: https://www.pythontutorial.net/tkinter/tkinter-ttk/

import tkinter as tk
from tkinter import ttk
from turtle import bgcolor, color

# creating an instance of tk.TK call to create the application window
root = tk.Tk() # root can be any other name. root is by convension
root.geometry("800x600")

# place a tk label on the root window
tk_message = tk.Label(root, text="Hello, World TK!", font=("Helvetica", 20))
tk_message.pack()

# place a ttk label on the root window
ttk_message = ttk.Label(root, text="Hello, World TTK!", background="green", border=3, foreground="black", relief="raised") #flat, groove, raised, ridge, solid, or sunken
ttk_message.pack(ipadx=10, ipady=20) #internal padding x for left and right and y for top and bottom


ttk_messagefill = ttk.Label(root, text="Hello World - fill option", foreground="red", background="red", border=2).pack(ipadx=20, ipady=20, fill=tk.X) 
#fill= tk.BOTH, tk.X, tk.Y; 

# lable with image
photo = tk.PhotoImage(file='ASD/Examples/Widgets/uwe_logo.png')
image_label = ttk.Label(root, image=photo, text='UWE', compound='top', padding=5) 
# compound option specifies the position of the image relative to the text. 
#top, bottom, left, none, text, image ... none is like alt_text
image_label.pack(expand=True) #expand=True should allow the widget to expand and take all available space in Window / Frame



root1 = tk.Tk()
root1.geometry("350x200+900+600")

# box 1
box1 = tk.Label(root1, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=10, ipady=10, fill=tk.X)

# box 2
box2 = tk.Label(root1, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=10, ipady=10, fill=tk.X)

# box 3
box3 = tk.Label(root1, text="Box 3", bg="blue", fg="white", )
box3.pack(ipadx=10, ipady=10, fill=tk.X)

# box 4
box4 = tk.Label(root1, text="Box 4", bg="cyan", fg="black", )
box4.pack(ipadx=10, ipady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

# box 5
box5 = tk.Label(root1, text="Box 5", bg="purple", fg="white", )
box5.pack(ipadx=10, ipady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

# keep the window displaying
root1.mainloop()

# keep the window displaying
root.mainloop()