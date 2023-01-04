#source: https://www.pythontutorial.net/tkinter/tkinter-listbox/
from tkinter import *
#import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = Tk()
root.title('Listbox Example')


# create a list box
langs = ['Bristol', 'Birmingham', 'Manchester', 'London', 'Glasgow', 'Portsmouth', 'Liverpool', 'Kent', 'New Castle']

var = Variable(value=langs)

listbox = Listbox(
    root,
    listvariable=var,
    height=6,   #show six rows without needing scrollbar
    selectmode=SINGLE
    #selectmode=tk.EXTENDED  #allow multiple adjacent lines selection; 
                            # BROWSE - single selection with dragging mouse - default; 
                            # SINGLE - single line selection without dragging mouse; 
                            # MULTIPLE - number of lines and toggling usnig mouse clicks.
)

listbox.pack(expand=True, fill=BOTH, side=LEFT)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient=VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=LEFT, expand=True, fill=Y)

#callback
def items_selected(event):
    # get all selected indices 
    selected_indices = listbox.curselection()
    # get selected items... loop to go through all selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()