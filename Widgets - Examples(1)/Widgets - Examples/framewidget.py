# More details about frame: https://www.pythontutorial.net/tkinter/tkinter-frame/

# GUI Design: 
# Row 0 has three frames. 
# Frame 1 in Column 0, Frame 2 in Column 1, Frame 3 in Column 2
# -- Frame 1: 
# 	-- has labels and fields for Name and City. 
	# -- has two check boxes: Python and Java
# -- Frame 2:
# 	-- has three buttons
# -- Frame 3:
# 	-- has three buttons
# 
# Row 1 has one frame Frame 4. 
# -- Frame 4:
# 	-- has one label, one text field and one button



import tkinter as tk
from tkinter import RAISED, RIDGE, ttk, TclError, Text

def create_frame_1(container):    
    frame1 = ttk.Frame(container)

    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=3)
    
    ttk.Label(frame1, text='Name:').grid(column=0, row=0, sticky=tk.W)
    name_entry = ttk.Entry(frame1, width=30)
    name_entry.focus()
    name_entry.grid(column=1, row=0, sticky=tk.W)
   
    ttk.Label(frame1, text='City:').grid(column=0, row=1, sticky=tk.W)
    city_entry = ttk.Entry(frame1, width=30)
    city_entry.grid(column=1, row=1, sticky=tk.W)
    
    pythonlanguage = tk.StringVar()
    pythonlanguage_check = ttk.Checkbutton(
        frame1,
        text='Python',
        variable=pythonlanguage,
        command=lambda: print(pythonlanguage.get()))
    pythonlanguage_check.grid(column=0, row=2, sticky=tk.W)

    javalanguage = tk.StringVar()
    javalanguage_check = ttk.Checkbutton(
        frame1,
        variable=javalanguage,
        text='Java',
        command=lambda: print(javalanguage.get()))
    javalanguage_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame1.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame1

def create_frame_2(container):
    frame2 = ttk.Frame(container, borderwidth=1, relief=RIDGE, padding=5)

    frame2.columnconfigure(0, weight=2)    

    ttk.Button(frame2, text='Save').grid(column=0, row=0)
    ttk.Button(frame2, text='Clear').grid(column=0, row=1)
    ttk.Button(frame2, text='Delete').grid(column=0, row=2)
    ttk.Button(frame2, text='Archive').grid(column=0, row=3)

    for widget in frame2.winfo_children():
        widget.grid(padx=5, pady=5)    

    return frame2

def create_frame_3(container):
    frame3 = ttk.Frame(container)

    frame3.columnconfigure(0, weight=1)
    
    ttk.Button(frame3, text='Next').grid(column=0, row=0)
    ttk.Button(frame3, text='Previous').grid(column=0, row=1)
    ttk.Button(frame3, text='Close').grid(column=0, row=2)

    for widget in frame3.winfo_children():
        widget.grid(padx=5, pady=5)    

    return frame3

def create_frame_4(container):
    frame4 = ttk.Frame(container, borderwidth=2, relief=RAISED, padding=5)

    frame4.columnconfigure(0, weight=7)

    ttk.Label(frame4, text='Comments:').grid(row=0, sticky=tk.W)
    tk.Text(frame4, height=6).grid(row=1)
    ttk.Button(frame4, text='Save Comments').grid(row=2, sticky=tk.W)

    for widget in frame4.winfo_children():
        widget.grid(padx=5, pady=5)    
    
    return frame4


def create_main_window():
    root = tk.Tk()
    root.title('Favourite Language')    
    root.resizable(0,0)

    try:
        root.attributes('-toolwindow', True)
    except TclError:
        print(' - toolwindow Not supported on your platform')
    
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=2)
    root.columnconfigure(2, weight=1)

    frame_1 = create_frame_1(root)
    frame_1.grid(column=0, row=0)

    frame_2 = create_frame_2(root)
    frame_2.grid(column=1, row=0)

    frame_3 = create_frame_3(root)
    frame_3.grid(column=2, row=0)

    frame_4 = create_frame_4(root)
    frame_4.grid(row=1, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()







