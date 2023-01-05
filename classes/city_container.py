import city


class Cities():
    __instance = None

    __cities = dict()

    def __init__(self):
        if Cities.__instance:
            raise Exception("there can only be one Conn instance!")

        Cities.__instance = self

    def __getitem__(self, key: str):
        return Cities.__cities[key]

    def __setitem__(self, key: str, value: city.City):
        Cities.__cities[key] = value

    def get_cities(self):
        return Cities.__cities

    def add_city(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        Cities.__cities[city_name] = city.City(
            city_name, morning_price, afternoon_price, evening_price)
