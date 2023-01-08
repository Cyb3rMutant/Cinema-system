"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
class Screen(object):
    def __init__(self, screen_id, num_vip_seats, num_upper_seats, num_lower_seats, screen_number):

        self.__screen_id = screen_id

        self.__num_vip_seats = num_vip_seats

        self.__num_upper_seats = num_upper_seats

        self.__num_lower_seats = num_lower_seats

        self.__screen_number = screen_number

    def get_screen_id(self):
        return self.__screen_id

    def get_num_vip_seats(self):
        return self.__num_vip_seats

    def get_num_upper_seats(self):
        return self.__num_upper_seats

    def get_num_lower_seats(self):
        return self.__num_lower_seats

    def get_screen_number(self):
        return self.__screen_number

    def __str__(self):
        return "Screen number %d" % self.__screen_number
