import cinema


class User():
    def __init__(self, name: str, id: int, branch: cinema.Cinema):

        self.__name = name

        self.__id = id

        self.__branch = branch

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_branch(self):
        return self.__branch
