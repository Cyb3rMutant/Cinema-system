import payment
from dbfunc import conn


class Customer(object):
    def __init__(self, name, phone, email):

        self.__name = name

        self.__phone = phone

        self.__email = email

        # payment = conn.select(
        #     "SELECT * FROM PAYMENTS WHERE CUSTOMER_EMAIL=%s", (self.__email,))

        # self.__payment = payment.Payment(
        #     payment[0], payment[1], payment[2], payment[3])

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email
