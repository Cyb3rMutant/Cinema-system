import booking_upper_hall


class Booking_vip_hall(booking_upper_hall.Booking_upper_hall):
    seat_type = "vip"

    def __init__(self, booking_reference, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_vip_hall, self).__init__(booking_reference, show,
                                               number_of_seats, date_of_booking, city_price, customer)
        show.set_available_vip_seats(number_of_seats)

    def calc_price(self, city_price):
        b = booking_upper_hall.Booking_upper_hall.calc_price(self, city_price)
        return b+b*0.2

    def check_seats(self):
        return self.__show.get_available_vip_seats() < 0

    def as_list(self):
        return [self._booking_reference, self._number_of_seats, self._date_of_booking, self._price, self._show.get_show_id(), "vip", self._customer.get_email()]

    def __del__(self):
        self._show.set_available_vip_seats(-self._number_of_seats)
