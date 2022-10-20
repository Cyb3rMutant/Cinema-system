class Seat():
    def __init__(self, seat_number: int, seat_type: str):

        self.__seat_number = seat_number

        self.__seat_type = seat_type

    def get_seat_number(self):
        return self.__seat_number

    def get_seat_type(self):
        return self.__seat_type
