"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
class Film(object):
    def __init__(self, title, rating, genre, year, age_rating, duration, description, cast):

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

    def get_description(self):
        return self.__description

    def get_cast(self):
        return self.__cast

    def __str__(self):
        return f"{self.__title}"
