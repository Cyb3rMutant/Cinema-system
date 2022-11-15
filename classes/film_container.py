from film import Film
from dbfunc import conn
from container import Container


class Film_container(Container):

    def __init__(self):
        super(Container, self).__init__()
        self.__elements = dict()

        films = conn.select("SELECT * FROM FILMS;")

        for film in films:
            self.__elements[film[0]](film(film[0], film[1], film[2], film[3]))

    def add_element(self, film_title: str, film_rating: float, film_genre: list, film_year: str, film_age_rating: str, film_duration: int, film_description: str, film_cast: list):
        conn.insert("INSERT INTO FILMS VALUES (%s, %f, %s, %s, %s, %d, %s, %s);",
                    (film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast,))

        self.__elements[film_title](
            Film(film_title, film_rating, film_genre, film_year, film_age_rating, film_duration, film_description, film_cast))
