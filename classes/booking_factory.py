import booking_lower_hall
import booking_upper_hall
import booking_vip_hall


class Booking_factory(object):
    def get_booking_seat_hall(self, type):
        types = {
            "lower_hall": booking_lower_hall.Booking_lower_hall,
            "upper_hall": booking_upper_hall.Booking_upper_hall,
            "vip": booking_vip_hall.Booking_vip_hall
        }

        if type not in types:
            raise Exception("%s booking type does not exist" % type)

        return types[type]
