class Controller():
    def __init__(self):
        self.__model = None
        self.__view = None

    def set_model(self, model):
        self.__model = model

    def set_view(self, view):
        self.__view = view

    def login(self, username, password):
        data = self.__model.validate_login(username, password)
        if (data == -1):
            self.__view.show_error("User doesnt exist.")
        elif (data == 0):
            self.__view.show_error("Incorrect username or password.")
        else:
            self.__view.loggedin(data)
