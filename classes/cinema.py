from screen import Screen


class Cinema():
    def __init__(self, cinema_id: int, address: str, screens: list):

        self.__cinema_id = cinema_id

        self.__address = address

        self.__screens = screens

    def get_cinema_id(self):
        return self.__cinema_id

    def get_address(self):
        return self.__address

    def get_screens(self):
        return self.__screens
