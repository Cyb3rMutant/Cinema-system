#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-command/

import tkinter as tk
from tkinter import ttk
from random import randint
from tkinter.messagebox import showinfo

root = tk.Tk()

# callback function with parameters
def selectwinner(options):
    givenoptions = ['Rock', 'Paper', 'Scissors']
    selection_index = randint(0,2)
    if givenoptions[selection_index] == options:
        print('Well done! ', options, ' Won!')
    else:
        print('Better luck next time! ', options)

    """
    #Disable when Rock is clicked and enable when Paper or Scissors are clicked but it's not working! 
    if options == 'Rock':
        tempButton.state(['disabled'])
    else:
        tempButton.state(['!disabled'])
    """
        
# Use lambda function if you want to pass parameters to command binding callback function 
ttk.Button(root, text='Rock', command=lambda: selectwinner('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: selectwinner('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: selectwinner('Scissors')).pack()

tempButton = ttk.Button(root, text='No Action').pack()

# Use lamda function if there is single expression to bind with command
ttk.Button(root, text='Quit', command=lambda: root.quit()).pack() 

# Image on button
def download_clicked():
    showinfo(title='Information', message='Download button is clicked!')

download_icon = tk.PhotoImage(file='ASD/Examples/Widgets/download.png')
download_button = ttk.Button(root, image=download_icon, command=download_clicked).pack(ipadx=5, ipady=5, expand=True)


# Image and text on button by using compound
download_button1 = ttk.Button(root, image=download_icon, text='Download', compound=tk.RIGHT, command=download_clicked).pack(ipadx=5, ipady=5, expand=True)


root.mainloop()

"""
# Simple approach... simple callback function 
def button_clicked():
    print('Button clicked')

# Simple approach... command binding - check command attribute is 
# assigned function name only without () 
button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()
"""