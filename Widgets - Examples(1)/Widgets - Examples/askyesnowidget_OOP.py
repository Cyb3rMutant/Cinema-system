#Source: https://www.pythontutorial.net/tkinter/tkinter-askyesno/


from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno

class App(Tk):
    def __init__(self):
        super().__init__()


        # create the root window        
        self.title('Tkinter Yes/No Dialog')
        self.geometry('300x150')

        button = ttk.Button(self, text='Quit', command=self.confirm)
        button.pack(expand=True)


# click event handler
    def confirm(self):
        answer = askyesno(title='confirmation',
                    message='Are you sure that you want to quit?')
        if answer:
            self.destroy()




# start the app
if __name__ == '__main__':
    app = App()
    app.mainloop()