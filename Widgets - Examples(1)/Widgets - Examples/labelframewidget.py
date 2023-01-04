#Source: https://www.pythontutorial.net/tkinter/tkinter-labelframe/

#Label frame is a container that can contain other related widgets e.g., grouping
#radio buttons widget and place the group on a lableframe

#import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

# root window
root = Tk()

# configure the root window
root.geometry('400x200')
root.resizable(False, False)
root.title('LabelFrame Demo')

# label frame
lf = ttk.LabelFrame(root, text='Alignment')
lf.grid(column=0, row=0, padx=20, pady=20)

alignment_var = StringVar()
alignments = ('Left', 'Center', 'Right')

# create radio buttons and place them on the label frame

grid_column = 0
for alignment in alignments:
    # create a radio button
    radio = ttk.Radiobutton(lf, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid column
    grid_column += 1

def option_selected():       
    messagebox.showinfo(title='Result', message=alignment_var.get())


button = ttk.Button(lf, text='Get Option Value', command=option_selected)
button.grid(row=1, columnspan=3)


root.mainloop()