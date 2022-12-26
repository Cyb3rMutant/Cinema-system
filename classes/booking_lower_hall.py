import booking


class Booking_lower_hall(booking.Booking):
    seat_type = "lower"

    def __init__(self, booking_reference, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_lower_hall, self).__init__(booking_reference, show,
                                                 number_of_seats, date_of_booking, city_price, customer)
        show.set_available_lower_seats(number_of_seats)

    def calc_price(self, city_price):
        return city_price

    def as_list(self):
        return [self._booking_reference, self._number_of_seats, self._date_of_booking, self._price, self._show.get_show_id(), "lower", self._customer.get_email()]

    def __del__(self):
        self._show.set_available_lower_seats(-self._number_of_seats)
        print("done")
