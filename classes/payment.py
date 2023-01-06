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
