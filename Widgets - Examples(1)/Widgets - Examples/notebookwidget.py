# Adapted from Source: https://www.pythontutorial.net/tkinter/tkinter-notebook/

from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, relief='sunken', height=280)
frame2 = ttk.Frame(notebook, width=400, relief='raised', height=280)
frame3 = ttk.Frame(notebook, width=400, relief='groove', height=280)
frame4 = ttk.Frame(notebook, width=400, relief='solid', height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

button = Button(frame1, text='Say Hello', command=lambda: print('Hello World'))
button.pack(side=LEFT)
# add frames to notebook

button = Button(frame1, text='Hide Reports', command=lambda: notebook.hide(3))
button.pack(side=LEFT)
# notebook.hide(0) #temporarily removes the tab from the Notebook;
# index starts at 0.

# to show the tab will need to call add method again.
button = Button(frame1, text='Show Reports',
                command=lambda: notebook.add(frame4))
button.pack(side=LEFT)

button = Button(frame4, text='Quit', command=lambda: quit())
button.pack(side=LEFT)

notebook.add(frame1, text='Cities')
notebook.add(frame2, text='Showings')
notebook.add(frame3, text='Bookings')
notebook.add(frame4, text='Reports')

# notebook.forget permanently removes the child widget from the notebook.

root.mainloop()
