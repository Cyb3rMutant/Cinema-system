from city import City
from dbfunc import conn
from container import Container


class City_container(Container):

    def __init__(self):
        super(Container, self).__init__()
        self.__elements = dict()

        cities = conn.select("SELECT * FROM CITIES;")

        for city in cities:
            self.__elements[city[0]] = (
                City(city[0], city[1], city[2], city[3]))

    def add_element(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):

        conn.insert("INSERT INTO CITIES VALUES (%s, %s, %s, %s);",
                    (city_name, morning_price, afternoon_price, evening_price,))

        self.__elements[city_name] = (
            City(city_name, morning_price, afternoon_price, evening_price))
