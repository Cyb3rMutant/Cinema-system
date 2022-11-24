import film
from dbfunc import conn


class Films_container():
    __instance = None

    def __init__(self):
        if Films_container.__instance:
            raise Exception("there can only be one Conn instance!")

        Films_container.__instance = self

        self.__films = dict()

        films = conn.select("SELECT * FROM films;")

        for film in films:
            self.__films[film[0]] = (
                film.Film(film[0], film[1], film[2], film[3]))

    def get_films(self):
        return self.__films

    def add_film(self, film_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        conn.insert("INSERT INTO films VALUES (%s, %s, %s, %s);",
                    (film_name, morning_price, afternoon_price, evening_price,))

        self.__films[film_name] = (
            film.Film(film_name, morning_price, afternoon_price, evening_price))

    def remove_film(self, film_name:str):
        
        if film_name in self.__films:
            conn.delete("DELETE FROM FILMS WHERE FILM_TITLE = %s;", (film_name,))
            del self.__films(film_name)
        else:
            print("Film doesn't exist")
