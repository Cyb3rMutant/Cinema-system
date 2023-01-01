import booking_lower_hall


class Booking_upper_hall(booking_lower_hall.Booking_lower_hall):
    seat_type = "upper"

    def __init__(self, booking_reference, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_upper_hall, self).__init__(booking_reference, show,
                                                 number_of_seats, date_of_booking, city_price, customer)
        show.set_available_upper_seats(number_of_seats)

    def calc_price(self, city_price):
        b = booking_lower_hall.Booking_lower_hall.calc_price(self, city_price)
        return b+b*0.2

    def check_seats(self):
        return self._show.get_available_upper_seats() < 0

    def as_list(self):
        return [self._booking_reference, self._number_of_seats, self._date_of_booking, self._price, self._show.get_show_id(), "upper"]

    def __del__(self):
        self._show.set_available_upper_seats(-self._number_of_seats)
