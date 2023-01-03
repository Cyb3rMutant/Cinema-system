import film
from dbfunc import conn


class Films():
    __instance = None

    __films = dict()

    def __init__(self):
        if Films.__instance:
            raise Exception("there can only be one Conn instance!")

        Films.__instance = self

    def __getitem__(self, key):
        return Films.__films[key]

    def __setitem__(self, key: str, value: film.Film):
        Films.__films[key] = value

    @staticmethod
    def get_film(f):
        return Films.__films[f]

    def get_films(self):
        return Films.__films

    def add_film(self, film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast):
        Films.__films[film_title] = film.Film(
            film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast)
