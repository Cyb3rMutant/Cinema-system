import user
import cinema


class Booking_staff(user.User):
    def __init__(self, name: str, id: int, branch: cinema.Cinema):
        super(Booking_staff, self).__init__(name, id, branch)
