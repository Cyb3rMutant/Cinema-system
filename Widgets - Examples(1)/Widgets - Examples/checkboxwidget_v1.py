#Source: https://www.pythontutorial.net/tkinter/tkinter-checkbox/

# a callback can be associated and called when checked or unchecked 
from tkinter import *
from tkinter import messagebox

#callback
def python_check_changed():   
    temp = var1.get() 
    #print('Python Checkbox value changed to: ' + temp)
    messagebox.showinfo(title='Python Checkbox Result', message=temp)

def java_check_changed():    
    temp = var2.get()
    #print('Java Checkbox value changed to: ' + temp)
    messagebox.showinfo(title='Java Checkbox Result', message=temp)

root = Tk()
root.title('Checkbox example')
root.geometry('200x70')

var1 = StringVar()
#default values for selected is 1 and when unselected then 0; 
#if other values are needed then onvalue and offvalue can be used. 
#for demo purposes I am using text string for onvalue and offvalue fields
#If the linked variable doesn’t exist, or its value is neither the on value nor off value, 
# the checkbox is in the indeterminate or tristate mode.
checkbox_v = Checkbutton(root, text='Want to learn Python', command=python_check_changed, variable=var1, onvalue='Agree for Python', offvalue='Disagree for Python')
checkbox_v.grid(row=0, sticky=W)

var2 = StringVar()
checkbox_v1 = Checkbutton(root, text='Want to learn Java', command=java_check_changed, variable=var2, onvalue='Java selected', offvalue='Java not selected')
checkbox_v1.grid(row=1, sticky=W)

#checkbox_v['state'] = 'disabled' #disabling checkbox
print(var1.get())   #getting varibale value 0 for not selected and 1 for selected
print(var2.get())

mainloop()