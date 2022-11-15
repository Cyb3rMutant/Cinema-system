from user import User


class Booking_staff(User):
    def __init__(self, name: str, id: int, branch: Cinema):
        super(Booking_staff, self).__init__(name, id, branch)
