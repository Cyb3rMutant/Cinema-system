import city
from dbfunc import conn


class Cities():
    __instance = None

    def __init__(self):
        if cities.__instance:
            raise Exception("there can only be one Conn instance!")

        Cities.__instance = self

        self.__cities = dict()

        cities = conn.select("SELECT * FROM CITIES;")

        for city in cities:
            self.__cities[city[0]] = (
                city.City(city[0], city[1], city[2], city[3]))

    def __getitem__(self, idx):
        return self.__cities[idx]

    def add_city(self, city_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        conn.insert("INSERT INTO CITIES VALUES (%s, %s, %s, %s);",
                    (city_name, morning_price, afternoon_price, evening_price,))

        self.__cities[city_name] = (
            city.City(city_name, morning_price, afternoon_price, evening_price))

    def remove_city(self, city_name: str):
        #removing city (ben)
        if city_name in self.__cities:
            #delete from database
            conn.delete("DELETE FROM CITIES WHERE CITY_NAME = %s;", (city_name))
            #delete from cities dictionary
            del self.__cities[city_name]
        else:
            print("City doesnt exist")  #print to terminal
