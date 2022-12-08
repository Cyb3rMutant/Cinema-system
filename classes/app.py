import tkinter as tk
import models
import guis
import controllers


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1350x800+0+0")
        self.configure(background="gainsboro")
        self.MainFrame = tk.Frame(
            self, bd=10, width=1350, height=800, bg='gainsboro', relief=tk.RIDGE)
        self.MainFrame.grid()

        self.HeaderFrame = tk.Frame(
            self.MainFrame, bd=10, width=1330, height=100, bg='gainsboro', relief=tk.RIDGE)
        self.HeaderFrame.config(bg='#333333')
        self.HeaderFrame.grid()
        # Header
        # Page Name is different for each class. We place them on the class itself. (Top Left Title)
        self.title_label = tk.Label(self.HeaderFrame, text="Horizon Cinemas",
                                    borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 16))
        self.title_label.place(x=443, y=5, width=443, height=70)
        self.branch_label = tk.Label(self.HeaderFrame, text="",
                                     borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 16))
        # Higher width overlaps border. Had to make it smaller and adjust with X
        self.branch_label.place(x=890, y=5, width=400)
        self.name_label = tk.Label(
            self.HeaderFrame, text="", borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 16))
        self.name_label.place(x=890, y=40, width=400)

        self.page_label = tk.Label(self.HeaderFrame, text="",
                                   borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 16))
        self.page_label.place(x=0, y=5, width=443, height=70)  # 443 = width/3

        self.BodyFrame = tk.Frame(
            self.MainFrame, bd=10, width=1330, height=680, bg="gainsboro", relief=tk.RIDGE)
        self.BodyFrame.grid()

        self.title('Login')
        self.resizable(0, 0)
        self.config(bg="#333333")

        model = models.Model()
        view = guis.Main_frame(self)

        controller = controllers.Controller(model, view)

        view.set_controller(controller)


App().mainloop()
