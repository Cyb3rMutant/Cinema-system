#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-separator/

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk

root = Tk()
root.title('ScrolledText example')
root.resizable(False,False)

Label(root, text='ScrolledText Widget and Separator').pack()

sep = ttk.Separator(root,orient='horizontal')
sep.pack(fill=X)

text_v = ScrolledText(root, height=10, width=50)
text_v.pack(fill=BOTH, side=LEFT, expand=True)

sep1 = ttk.Separator(root,orient='vertical')
sep1.pack(fill=Y, side=LEFT)

button = Button(root, text='Quit', command=lambda: quit())
button.pack(side=RIGHT)

root.mainloop()


