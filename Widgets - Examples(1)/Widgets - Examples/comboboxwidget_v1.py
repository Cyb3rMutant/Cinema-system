#Source https://www.pythontutorial.net/tkinter/tkinter-combobox/ 

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a city:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_city = tk.StringVar()
cities_cb = ttk.Combobox(root, textvariable=selected_city)

# setting the values of the cities_cb... These values may come from Database
cities_cb['values'] = ['Bristol', 'Birmingham', 'Manchester', 'London']

# prevent typing a value
cities_cb['state'] = 'readonly'

# place the widget
cities_cb.pack(fill=tk.X, padx=5, pady=5)

# bind the selected value changes
def cities_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_city.get()}!'
    )

cities_cb.bind('<<ComboboxSelected>>', cities_changed)

#To set the current value of the combobox
cities_cb.set('Bristol')



root.mainloop()