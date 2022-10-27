class Customer(object):
    def __init__(self, name: str, phone: str, email: str):

        self.__name = name

        self.__phone = phone

        self.__email = email

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email
