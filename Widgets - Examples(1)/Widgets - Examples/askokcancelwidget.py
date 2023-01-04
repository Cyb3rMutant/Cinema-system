#Source: https://www.pythontutorial.net/tkinter/tkinter-askokcancel/


from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# create the root window
root = Tk()
root.title('Tkinter OKCancel Dialog')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askokcancel(title='confirmation', message='All data will be deleted..', icon=WARNING)
    if answer:
        showinfo(title='Delete status', message='The data is successfully deleted.')
        

ttk.Button(root, text='Delete All', command=confirm).pack(expand=True)

# start the app
root.mainloop()