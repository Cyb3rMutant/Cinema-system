#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-askokcancel/

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# create the root window
class App(Tk):
    def __init__(self):
        super().__init__()
    
        self.title('Tkinter OKCancel Dialog')
        self.geometry('300x150')
        ttk.Button(self, text='Delete All', command=self.confirm).pack(expand=True)

    # click event handler
    def confirm(self):
        answer = askokcancel(title='confirmation', message='All data will be deleted..', icon=WARNING)
        if answer:
            #delete all data and show confirmation message
            showinfo(title='Delete status', message='The data is successfully deleted.')
        

# start the app
if __name__ == '__main__':
    app = App()
    app.mainloop()