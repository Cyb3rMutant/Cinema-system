from show import Show


class Screen():
    def __init__(self, screen_number: int, shows: list, num_vip_seats: int, num_upper_seats: int, num_lower_seats: int):

        self.__screen_number = screen_number

        self.__shows = shows

        self.__num_vip_seats = num_vip_seats

        self.__num_upper_seats = num_upper_seats

        self.__num_lower_seats = num_lower_seats

    def get_screen_number(self):
        return self.__screen_number

    def get_seats(self):
        return self.__seats

    def get_shows(self):
        return self.__shows

    def get_num_vip_seats(self):
        return self.__num_vip_seats

    def get_num_upper_seats(self):
        return self.__num_upper_seats

    def get_num_lower_seats(self):
        return self.__num_lower_seats
