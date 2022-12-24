import booking_upper_hall


class Booking_vip_hall(booking_upper_hall.Booking_upper_hall):
    def __init__(self, show, number_of_seats, date_of_booking, city_price, customer):
        super(Booking_vip_hall, self).__init__(
            show, number_of_seats, date_of_booking, city_price, customer)
        show.set_available_vip_seats(number_of_seats)

    def calc_price(self, city_price):
        return city_price+(booking_upper_hall.Booking_upper_hall.calc_price(self, city_price)*0.2)
