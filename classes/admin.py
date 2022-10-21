from booking_staff import Booking_staff
from cinema import Cinema


class Admin(Booking_staff):
    def __init__(self, name: str, id: int, branch: Cinema):
        super(Admin, self).__init__(name, id, branch)

    def generate_report(self):
        pass

    def add_listing(self):
        pass

    def remove_listing(self):
        pass

    def update_listing(self):
        pass
