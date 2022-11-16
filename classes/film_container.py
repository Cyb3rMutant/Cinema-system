import film
from dbfunc import conn


class Films():
    __instance = None

    def __init__(self):
        if Films.__instance:
            raise Exception("there can only be one Conn instance!")

        Films.__instance = self

        self.__films = dict()

        films = conn.select("SELECT * FROM films;")

        for film in films:
            self.__films[film[0]] = (
                film.Film(film[0], film[1], film[2], film[3]))

    def __getitem__(self, idx):
        return self.__films[idx]

    def add_film(self, film_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        conn.insert("INSERT INTO films VALUES (%s, %s, %s, %s);",
                    (film_name, morning_price, afternoon_price, evening_price,))

        self.__films[film_name] = (
            film.Film(film_name, morning_price, afternoon_price, evening_price))

    def remove_film(self):
        pass
