class Film():
    def __init__(self, title: str, rating: float, genre: list, year: str, age_rating: str, duration: int, description: str, cast: list):

        self.__title = title

        self.__rating = rating

        self.__genre = genre

        self.__year = year

        self.__age_rating = age_rating

        self.__duration = duration

        self.__description = description

        self.__cast = cast

    def get_title(self):
        return self.__title

    def get_rating(self):
        return self.__rating

    def get_genre(self):
        return self.__genre

    def get_year(self):
        return self.__year

    def get_age_rating(self):
        return self.__age_rating

    def get_duration(self):
        return self.__duration

    def get_decription(self):
        return self.__description

    def get_cast(self):
        return self.__cast
