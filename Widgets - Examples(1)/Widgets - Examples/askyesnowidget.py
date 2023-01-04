#Source: https://www.pythontutorial.net/tkinter/tkinter-askyesno/


from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
root = Tk()
root.title('Tkinter Yes/No Dialog')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to quit?')
    if answer:
        root.destroy()

ttk.Button(root, text='Quit', command=confirm).pack(expand=True)

# start the app
root.mainloop()