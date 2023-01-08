"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
class Payment(object):
    # ˅

    # ˄

    def __init__(self, name_on_card, card_number, expiry, cvv):

        self.__name_on_card = name_on_card

        self.__card_number = card_number

        self.__expiry = expiry

        self.__cvv = cvv

    def get_card_number(self):
        return "*****"+self.__card_number[-4:]

    def pay(self, amount):
        print(f"payment of {amount} complete")

    def refund(self, amount):
        print(f"refund of {amount} complete")
