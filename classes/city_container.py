import city
from dbfunc import conn


class Cities():
    __instance = None

    def __init__(self):
        if Cities.__instance:
            raise Exception("there can only be one Conn instance!")

        Cities.__instance = self

        self.__cities = dict()

    def __getitem__(self, key: str):
        return self.__cities[key]

    def __setitem__(self, key: str, value: city.City):
        self.__cities[key] = value

    def get_cities(self):
        return self.__cities

    def add_city(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        self.__cities[city_name] = (
            city.City(city_name, morning_price, afternoon_price, evening_price))

    def remove_city(self, city_name: str):
        # removing city (ben)
        if city_name in self.__cities:
            # delete from database
            conn.delete("DELETE FROM cities WHERE CITY_NAME = %s;", (city_name))
            # delete from cities dictionary
            self.__cities.pop[city_name]
        else:
            print("City doesnt exist")  # print to terminal
