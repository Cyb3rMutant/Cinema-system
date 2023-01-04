#Adapted from Source: https://www.pythontutorial.net/tkinter/tkinter-treeview/
#Treeview can be used to present data in tabular form or hierarchical form

#it holds a list of items and each item has one or more columns.
#first column may contain text/icon indicating whether it can be expansible or not.
#The remaining columns contain values of each row.
#the firstrow of treeview consists of headings for each column name

#1. import
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(Tk):
    def __init__(self):
        super().__init__()
        #2. create root window set options        
        self.title('Treeview demo')
        self.geometry('620x200')

        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        #3. define identifiers for columns
        columns = ('first_name', 'last_name', 'email')

        #4. create tree view widget
        #columns to column option and show='headings' hides the first column (column #0)
        #show values can be 'tree' - shows the column #0
        #                   'heading' - shows the header row
        #                   'tree headings' - shows both column #0 and the header row. this is default value.
        #                   '' - doesn't show the column 0 or the header row.

        tree = ttk.Treeview(self, columns=columns, show='headings')

        #5.  define headings
        tree.heading('first_name', text='First Name List')
        tree.heading('last_name', text='Last Name List')
        tree.heading('email', text='Email List')

        #6. generate sample data - tuples
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        #7. add data to the treeview
        for contact in contacts:
            tree.insert('', END, values=contact)

        #9. Bind <> to callback function
        tree.bind('<<TreeviewSelect>>', self.item_selected)

        #10. place treeview to root window
        tree.grid(row=0, column=0, sticky='nsew')

        #11. add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        return tree

        #8. define call back functio to handle <> event. 
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

        
if __name__ == '__main__':               
    app = App()
    #12. run the app
    app.mainloop()