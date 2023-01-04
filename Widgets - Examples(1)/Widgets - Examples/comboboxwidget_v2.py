#Adapted from source: https://www.pythontutorial.net/tkinter/tkinter-combobox/ 

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

#current_value = combox.get() #can also be used to get selected value
#current_var.set(new_value) # to set the value to associated variable
#combobox.set(new_value)

# prevent typing a value
cities_cb['state'] = 'readonly'
#cities_cb['state'] = 'normal' #alternative to readonly

# place the widget
cities_cb.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_cinema = tk.StringVar()
cinemas_cb = ttk.Combobox(root, textvariable=selected_cinema)
#cinemas['values'] = ['Vue', 'Cineplex', 'Showcase']
cinemas_cb['state'] = 'readonly'
cinemas_cb.pack(fill=tk.X, padx=5, pady=5)

# bind the selected value changes
def cities_changed(event):    

    #ideally the following values should be retrieved from DB
    #for demo purposes I am using an if-else structure
    if selected_city.get() == 'Bristol':
        cinemas_cb['values'] = ['Vue', 'Cineplex', 'Showcase']
    elif selected_city.get() == 'Birmingham':
        cinemas_cb['values'] = ['Vue', 'Cineplex', 'Showcase', 'Odean']
    elif selected_city.get() == 'Manchester':
        cinemas_cb['values'] = ['Vue', 'Cineplex', 'Showcase', 'Odean', 'Cerose']
    else:
        cinemas_cb['values'] = ['Vue', 'Cineplex', 'Showcase', 'Odean', 'Cerose', 'Metropolitan', 'RoyalShow']

def cinema_changed(event):
    
    showinfo(
        title='Result',
        message=f'You selected city: {selected_city.get()} and cinema: {selected_cinema.get()}!'
    )

cities_cb.bind('<<ComboboxSelected>>', cities_changed)
cinemas_cb.bind('<<ComboboxSelected>>', cinema_changed)


root.mainloop()