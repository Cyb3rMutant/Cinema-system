class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login(self, username, password):
        data = self.model.validate_login(username, password)
        if (data == -1):
            self.view.show_error("User doesnt exist.")
        elif (data == 0):
            self.view.show_error("Incorrect username or password.")
        else:
            self.view.loggedin(data)
