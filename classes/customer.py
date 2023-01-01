import payment
from dbfunc import conn


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

    def set_payment(self, payment):
        self.__payment = payment
