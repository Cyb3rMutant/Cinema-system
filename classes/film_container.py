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

        for f in films:
            self.__films[f["FILM_TITLE"]] = (
                film.Film(f["FILM_TITLE"], f["FILM_RATING"], f["FILM_GENRE"], f["FILM_YEAR"], f["FILM_AGE_RATING"], f["FILM_DURATION"], f["FILM_DESCRIPTION"], f["FILM_CAST"]))

    def __getitem__(self, film_name):
        return self.__cities[film_name]

    def get_films(self):
        return self.__films

    def add_film(self, film_name: str, morning_price: int, afternoon_price: int, evening_price: int):
        conn.insert("INSERT INTO films VALUES (%s, %s, %s, %s);",
                    (film_name, morning_price, afternoon_price, evening_price,))

        self.__films[film_name] = (
            film.Film(film_name, morning_price, afternoon_price, evening_price))

    def remove_film(self, film_name: str):

        if film_name in self.__films:
            conn.delete(
                "DELETE FROM films WHERE FILM_TITLE = %s;", (film_name,))
            self.__films.pop(film_name)
        else:
            print("Film doesn't exist")


films = Films()
