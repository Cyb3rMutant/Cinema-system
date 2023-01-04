#Adapted from Source: 
# https://www.pythontutorial.net/tkinter/tkinter-notebook/
# https://www.pythontutorial.net/tkinter/tkinter-treeview/

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = Tk()
root.geometry('675x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=650, relief='sunken', height=280)
frame2 = ttk.Frame(notebook, width=650, relief='raised', height=280)
frame3 = ttk.Frame(notebook, width=650, relief='groove', height=280)
frame4 = ttk.Frame(notebook, width=650, relief='solid', height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

button = Button(frame1, text='Say Hello', command=lambda: print('Hello World'))
button.pack(side=LEFT)
# add frames to notebook

button = Button(frame1, text='Hide Reports', command=lambda: notebook.hide(3))
button.pack(side=LEFT)
#notebook.hide(0) #temporarily removes the tab from the Notebook; 
# index starts at 0.

#to show the tab will need to call add method again. 
button = Button(frame1, text='Show Reports', command=lambda: notebook.add(frame4))
button.pack(side=LEFT)

button = Button(frame4, text='Quit', command=lambda: quit())
button.pack(side=LEFT)

notebook.add(frame1, text='Cities')
notebook.add(frame2, text='Showings')
notebook.add(frame3, text='Bookings')
notebook.add(frame4, text='Reports')


#3. define identifiers for columns
columns = ('first_name', 'last_name', 'email')

#4. create tree view widget
#columns to column option and show='headings' hides the first column (column #0)
#show values can be 'tree' - shows the column #0
#                   'heading' - shows the header row
#                   'tree headings' - shows both column #0 and the header row. this is default value.
#                   '' - doesn't show the column 0 or the header row.

tree = ttk.Treeview(frame2, columns=columns, show='headings')

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

#8. define call back functio to handle <> event. 
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

#9. Bind <> to callback function
tree.bind('<<TreeviewSelect>>', item_selected)

#10. place treeview to root window
#tree.grid(row=0, column=0, sticky='nsew')
tree.pack(side=LEFT)

#11. add a scrollbar
scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=tree.yview)

#scrollbar.grid(row=0, column=1, sticky='ns')
scrollbar.pack(side=RIGHT, fill=Y)
tree.configure(yscroll=scrollbar.set)
#tree['yscrollcommand'] = scrollbar.set 


#12. run the app
root.mainloop()