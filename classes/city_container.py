import city
from dbfunc import conn


class Cities():
    __instance = None

    def __init__(self):
        if Cities.__instance:
            raise Exception("there can only be one Conn instance!")

        Cities.__instance = self

        self.__cities = dict()

        cities = conn.select("SELECT * FROM cities;")

        for c in cities:
            self.__cities[c["CITY_NAME"]] = (
                city.City(c["CITY_NAME"], c["CITY_MORNING_PRICE"], c["CITY_AFTERNOON_PRICE"], c["CITY_EVENING_PRICE"]))

    def __getitem__(self, city_name):
        return self.__cities[city_name]

    def get_cities(self):
        return self.__cities

    def add_city(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        conn.insert("INSERT INTO cities VALUES (%s, %s, %s, %s);",
                    (city_name, morning_price, afternoon_price, evening_price,))

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


cities = Cities()
