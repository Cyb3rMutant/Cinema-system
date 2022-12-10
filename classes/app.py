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
        self.main_frame = tk.Frame(
            self, bd=10, width=1350, height=800, bg='gainsboro', relief=tk.RIDGE)
        self.main_frame.grid()

        self.header_frame = tk.Frame(
            self.main_frame, bd=10, width=1330, height=100, bg='gainsboro', relief=tk.RIDGE)
        self.header_frame.config(bg='#333333')
        self.header_frame.grid()
        # Header
        # Page Name is different for each class. We place them on the class itself. (Top Left Title)
        self.title_label = tk.Label(self.header_frame, text="Horizon Cinemas",
                                    borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 24))
        self.title_label.place(x=443, y=5, width=443, height=70)
        self.branch_label = tk.Label(self.header_frame, text="",
                                     borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 20))
        # Higher width overlaps border. Had to make it smaller and adjust with X
        self.branch_label.place(x=890, y=5, width=400)
        self.name_label = tk.Label(
            self.header_frame, text="", borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 20))
        self.name_label.place(x=890, y=40, width=400)

        self.page_label = tk.Label(self.header_frame, text="",
                                   borderwidth=1, bg='#333333', fg='#DD2424', font=("Arial", 24))
        self.page_label.place(x=0, y=5, width=443, height=70)  # 443 = width/3

        self.body_frame = tk.Frame(
            self.main_frame, bd=10, width=1330, height=680, bg="gainsboro", relief=tk.RIDGE)
        self.body_frame.grid()

        self.title('Horizon Cinemas system')
        self.resizable(0, 0)
        self.config(bg="#333333")

        controller = controllers.Controller()
        model = models.Model()
        view = guis.Main_frame(self, controller)

        controller.set_model(model)
        controller.set_view(view)


App().mainloop()
