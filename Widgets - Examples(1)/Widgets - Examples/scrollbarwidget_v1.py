#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-scrollbar/
from nntplib import NNTP_SSL_PORT
from tkinter import *
from tkinter import ttk
from turtle import st


#Scrollbar is independent widget
#Process to use scrollbar:
# 1. create scrollbar widet
# 2. link scrollbar with scrollable widget (which is already defined)

root = Tk()
root.title('Text with Scrollbar example')
root.resizable(False,False)

# apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lable_v = Label(root, text='Text Widget with Scrollbar')
lable_v.grid(row=0, column=0, sticky=EW)


text_v = Text(root, height=10)
text_v.grid(row=1, column=0, sticky=EW)

#creating scroobal, orientation and linking with text field 
#command can be xview or yview
#orient can be vertical or horizontal
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text_v.yview)
scrollbar.grid(row=1, column=1, sticky=NS)

# Scrollbar widget also needs to communicate back to the scrollbar about the 
# percentage of the entire content area that is currently visible. 
# To communicate back to the scrollbar the options xscrollcommand/yscrollcommand can be
# assigned scrollbar.set
text_v['yscrollcommand'] = scrollbar.set

#Initial or default contents on position 1.0 i.e. line.column
for i in range (1,50):
    position = f'{i}.0'
    text_v.insert(position, f'Line {i}\n')

#text_v.insert('1.0', 'This is a text widget default text line 1\n')
#text_v.insert('2.0', 'This is a text widget default text line 2\n')
#text_v.insert('3.0', 'This is a text widget default text line 3\n')

root.mainloop()
