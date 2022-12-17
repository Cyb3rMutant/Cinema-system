import tkinter as tk


class Example(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas = tk.Canvas(self)
        canvas.pack()
        self.startGame = tk.Button(canvas, text="Start", background='white', font=("Helvetica"),
                                   command=lambda: self.hide_me(self.startGame))
        self.startGame.place(x=150, y=100)

    def hide_me(self, event):
        print('hide me')
        event.place_forget()


if __name__ == "__main__":
    Example().mainloop()
