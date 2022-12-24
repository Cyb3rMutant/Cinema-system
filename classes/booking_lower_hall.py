import booking


class Booking_lower_hall(booking.Booking):
    def __init__(self, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_lower_hall, self).__init__(
            show, number_of_seats, date_of_booking, city_price, customer)
        show.set_available_lower_seats(number_of_seats)

    def calc_price(self, city_price):
        return city_price
