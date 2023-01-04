#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-radio-button/

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def option_selected():   
    #print('Result: ' + var1.get())
    messagebox.showinfo(title='Result', message=var1.get())

root = Tk()
root.title('Radio Button example')
root.geometry('300x200')

var1 = StringVar()

radiobutton1 = ttk.Radiobutton(root, text='Want to learn Python', variable=var1, value='Python selected')
radiobutton1.pack(fill='x', padx=5, pady=5)
radiobutton1.invoke() #default selection - same as clicked the button
#radiobutton1.select() #will only work with tk.Radiobutton
#radiobutton1.deselect() #will only work with tk.Radiobutton

radiobutton2 = ttk.Radiobutton(root, text='Want to learn Java', variable=var1, value='Java selected')
radiobutton2.pack(fill='x', padx=5, pady=5)

radiobutton3 = ttk.Radiobutton(root, text='Want to learn C++', variable=var1, value='C++ selected')
radiobutton3.pack(fill='x', padx=5, pady=5)

button = ttk.Button(root, text='Get Option Value', command=option_selected)
button.pack(fill='x', padx=5, pady=5)


mainloop()