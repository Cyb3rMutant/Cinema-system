import booking_staff
import cinema


class Admin(booking_staff.Booking_staff):
    def __init__(self, name: str, id: int, branch: cinema.Cinema):
        super(Admin, self).__init__(name, id, branch)
