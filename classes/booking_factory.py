import booking_lower_hall
import booking_upper_hall
import booking_vip_hall


class Booking_factory(object):
    @staticmethod
    def get_booking_seat_hall(type):
        types = {
            "lower": booking_lower_hall.Booking_lower_hall,
            "upper": booking_upper_hall.Booking_upper_hall,
            "vip": booking_vip_hall.Booking_vip_hall
        }

        if type not in types:
            raise Exception("%s booking type does not exist" % type)

        return types[type]
