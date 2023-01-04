#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-scrolledtext/

#scrolledtext is different from creating a text widget and scrollbar
# and linking them together. 

#scrolledtext has some properties similar to text
#it uses a Frame widget to hold the scrolledtext widget in a container
#so pack, grid and place are restricted to Frame.

from tkinter import *
from tkinter.scrolledtext import ScrolledText

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('ScrolledText example')
        self.resizable(False,False)
        Label(self, text='ScrolledText Widget').pack()
        text_v = ScrolledText(self, height=10, width=50)
        text_v.pack(fill=BOTH, side=LEFT, expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()


