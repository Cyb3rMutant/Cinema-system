#Source: https://www.pythontutorial.net/tkinter/tkinter-menu/

import tkinter as tk
from tkinter import Menu

#1. root window
root = tk.Tk()
root.title('Menu Demo')

#2. create a menubar and assign it to menu option of the root window
menubar = Menu(root)
root.config(menu=menubar)
#for each top-level window there can be only one menu bar

#3. create a menu whose container is menubar
file_menu = Menu(menubar, tearoff=0) #teraoff=0 to remove default dashed line

#4. add menu items to the menu
file_menu.add_command(label='New', command=lambda: print('New menu clicked') )
file_menu.add_command(label='Open', command=lambda: print('Open menu clicked'))
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

#5. add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu, underline=0) 
#underline option allows to create a keyboard shortcut. 
# It specifies the character position that should be underlined.
# In above case Alt+F is the short cut

#6. create another menu Aboutus ... notice menubar is now parent 
aboutus_menu = Menu(menubar, tearoff=0)

aboutus_menu.add_command(label='Who are we?', command=lambda: print('Who are we clicked'))
aboutus_menu.add_command(label='About us', command=lambda: print('About us clicked'))
menubar.add_cascade(label='About', menu=aboutus_menu)

#7. create submenu... notice aboutus_menu is now parent
sub_menu = Menu(aboutus_menu, tearoff=0)
sub_menu.add_command(label='History', command=lambda: print('History clicked'))
sub_menu.add_command(label='Vision', command=lambda: print('Vision clicked'))
sub_menu.add_command(label='Governors', command=lambda: print('Governors clicked'))

#8. create submenu... notice aboutus_menu is now parent
aboutus_menu.add_cascade(label='Details', menu=sub_menu)
root.mainloop()