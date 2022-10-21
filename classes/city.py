from cinema import Cinema


class City():
    def __init__(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int, cinemas: list):

        self.__city_name = city_name

        self.__morning_price = morning_price

        self.__afternoon_price = afternoon_price

        self.__evening_price = evening_price

        self.__cinemas = list()

    def get_city_name(self):
        return self.__city_name

    def get_morning_price(self):
        return self.__morning_price

    def get_afternoon_price(self):
        return self.__afternoon_price

    def get_evening_price(self):
        return self.__evening_price

    def get_cinemas(self):
        return self.__cinemas
