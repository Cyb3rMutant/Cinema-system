#source = https://www.pythontutorial.net/tkinter/tkinter-window/
import tkinter as tk

#following code will create simple window
root = tk.Tk()
#root.mainloop() #mainloop keeps the window displaying


root.title('My App') #To replace default title 'tk' to 'My App'

window_title = root.title() #To get the title of the window 
print('Window Title is: ', window_title)

#root.mainloop()

#Changing widow size and location

#root.geometry('300x200+500+100') #width x height + xaxix + yaxix
#root.mainloop()

#To center the window on screen

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root.mainloop()

#Window resizing - by default window is resizable 
#yoy may specify maxsize or minsize of window
min_width = 150
min_height = 150
max_width = 400
max_height = 400
root.minsize(min_width, min_height)
root.maxsize(max_width, max_height)
#root.resizable(False, False) #will disable the option to resize window

#transparency of a window can be set by setting its alpha channel 
# ranging from 0.0 (fully transparent) to 1.0 (fully opaque)
root.attributes('-alpha',0.5)
#root.mainloop()


#if there are multiple windows then you may stack them
root.attributes('-topmost', 1) # will always keep root window at top
#other available options are: -alpha, -fullscreen, -modified, -notify, -titlepath, -topmost, -transparent, or -type
#root.attributes('-fullscreen', True)

#lift() and lower() methods can be used to move window up and down the stack
#window.lift()
#window.lift(another_window)
#window.lower()
#window.lower(another_window)


#chaging window's default icon 
#you need .ico file. jpg or png can be converted to ico file
root.iconbitmap('ASD/Examples/Widgets/cricket_ball_sport_game_icon_228605.ico')
root.mainloop()
