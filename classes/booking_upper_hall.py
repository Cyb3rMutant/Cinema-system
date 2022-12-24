import booking_lower_hall


class Booking_upper_hall(booking_lower_hall.Booking_lower_hall):
    def __init__(self, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_upper_hall, self).__init__(
            show, number_of_seats, date_of_booking, city_price, customer)
        show.set_available_upper_seats(number_of_seats)

    def calc_price(self, city_price):
        return city_price+(booking_lower_hall.Booking_lower_hall.calc_price(self, city_price)*0.2)
