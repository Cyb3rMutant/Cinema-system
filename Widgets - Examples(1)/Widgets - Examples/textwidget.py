#Adatped from Source: https://www.pythontutorial.net/tkinter/tkinter-text/
from tkinter import *

#Text widget is only availabe in Tkinter module not Tkinter.ttk

#text = tk.Text*master, conf={}, **kw)
#master is parent component of the text widget
#cnf is the dictionary that specifies widget's configutation
#kw is one or more keyword arguments used to configure text widget

root = Tk()
root.title('Text example')
#root.geometry('300x220')
root.resizable(0,0)

Label(root, text='Text Widget').pack()

text_v = Text(root, height=10)
text_v.pack()

#Initial or default contents on position 1.0 i.e. line.column
text_v.insert('1.0', 'This is a text widget default text line 1\n')
text_v.insert('2.0', 'This is a text widget default text line 2\n')
text_v.insert('3.0', 'This is a text widget default text line 3\n')

#We can retrieve value by using get(start position, end position) method e.g.,
#differet start and end positions can be passed to retrieve part of the contents
#text_value = text_v.get('1.0', 'end') #will retrieve everything from text widget
text_value = text_v.get('2.0', '3.0') #only retrieve line 2
print(text_value)
#You may disable the widget by setting the state option to disabled. 
# This will prevent users from changing contents 

text_v['state'] = 'disabled'
#You may enable the widget by setting the state option to normal. 
#text_v['state'] = 'normal'

root.mainloop()
