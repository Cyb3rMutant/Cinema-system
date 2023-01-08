"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
class Customer(object):
    def __init__(self, name, phone, email, payment=None):

        self.__name = name

        self.__phone = phone

        self.__email = email

        self.__payment = payment

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_payment(self):
        return self.__payment

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_payment(self, payment):
        self.__payment = payment
