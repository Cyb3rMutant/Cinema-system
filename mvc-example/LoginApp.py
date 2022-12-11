from loginView import *
from UserAccount_Model import *
from LoginController import *
from DataAccessObject import *
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x250")
        self.title('Login')
        self.resizable(0, 0)

        model = UserAccountModel()

        view = Login_View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        controller = Login_Controller(model, view)

        view.set_controller(controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()
