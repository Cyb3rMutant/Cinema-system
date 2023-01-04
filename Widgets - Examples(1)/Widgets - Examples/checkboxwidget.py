#Source: https://www.pythontutorial.net/tkinter/tkinter-checkbox/

# a callback can be associated and called when checked or unchecked 
from tkinter import *

root = Tk()
root.title('Checkbox example')
root.geometry('200x70')

var1 = IntVar()
checkbox_v = Checkbutton(root, text='Want to learn Python', variable=var1)
checkbox_v.grid(row=0, sticky=W)

var2 = IntVar()
checkbox_v1 = Checkbutton(root, text='Want to learn Java', variable=var2)
checkbox_v1.grid(row=1, sticky=W)

checkbox_v['state'] = 'disabled' #disabling checkbox
print(var1.get())   #getting varibale value 0 for not selected and 1 for selected
print(var2.get())

mainloop()