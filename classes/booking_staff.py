from cinema import Cinema
from user import User


class Booking_staff(User):
    def __init__(self, name: str, id: int, branch: Cinema):
        super(Booking_staff, self).__init__(name, id, branch)

    def book_ticket(self):
        pass

    def view_bookings(self):
        pass

    def view_film_listing(self):
        pass

    def cancel_booking(self):
        pass
