#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-panedwindow/
#import tkinter as tk
from tkinter import *
from tkinter import ttk

#pane window can divide the space of frame or a window.
#pane window is like a frame and can be used as container to hold (stack) child widgets
#pane bar is called sash and it has handle to drag it around.
#a pane is an area occupied by one child widget. 

root = Tk()
root.title('PanedWindow Demo')
#root.geometry('600x200')
root.resizable(1,1)

# change style to classic (Windows only) 
# to show the sash and handle
style = ttk.Style()
style.theme_use('classic')

#Example to separate one label and three listboxes. 

# paned windows
# for label
lw = ttk.PanedWindow(orient=VERTICAL) 
# for list boxes
pw = ttk.PanedWindow(orient=HORIZONTAL) #or VERTICAL is default

# left label
label = Label(root, text='Left Listbox')
label.pack(side=TOP)
lw.add(label)

# Left listbox
left_list = Listbox(root)
left_list.pack(side=LEFT)
pw.add(left_list)

# Right listbox
right_list = Listbox(root)
right_list.pack(side=LEFT)
pw.add(right_list)

# Third listbox
third_list = Listbox(root)
third_list.pack(side=LEFT)
pw.add(third_list)

# place the panedwindow on the root window
lw.pack(fill=BOTH, expand=True)
pw.pack(fill=BOTH, expand=True)

root.mainloop()