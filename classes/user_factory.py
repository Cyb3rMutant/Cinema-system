import booking_staff
import admin
import manager
from dbfunc import conn


class User_factory():
    @staticmethod
    def get_user_type(type: str):
        types = {"Booking_staff": booking_staff.Booking_staff,
                 "Admin": admin.Admin,
                 "Manager": manager.Manager}

        if type not in types:
            raise Exception("%s user type does not exist" % type)

        return types[type]


if __name__ == "__main__":
    admin = User_factory.get_user_type("m")("yazee", 1, None)
    print(type(admin))
