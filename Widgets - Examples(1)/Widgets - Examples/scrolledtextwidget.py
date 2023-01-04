#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-scrolledtext/

#scrolledtext is different from creating a text widget and scrollbar
# and linking them together. 

#scrolledtext has some properties similar to text
#it uses a Frame widget to hold the scrolledtext widget in a container
#so pack, grid and place are restricted to Frame.

from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('ScrolledText example')
root.resizable(False,False)

Label(root, text='ScrolledText Widget').pack()

text_v = ScrolledText(root, height=10, width=50)
text_v.pack(fill=BOTH, side=LEFT, expand=True)

root.mainloop()


