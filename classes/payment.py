class Payment(object):
    # ˅

    # ˄

    def __init__(self, name_on_card, card_number, expiry, cvv):

        self.__name_on_card = name_on_card

        self.__card_number = card_number

        self.__expiry = expiry

        self.__cvv = cvv

    def get_name_on_card(self):
        return self._name_on_card

    def get_card_number(self):
        return self._card_number

    def get_expiry_date(self):
        return self._expiry_date

    def get_cvv(self):
        return self._cvv
