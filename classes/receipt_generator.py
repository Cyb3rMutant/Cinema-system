"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""
class Receipt_generator():
    def gen_receipt(booking, user):
        customer = booking.get_customer()
        payment = customer.get_payment()

        return f"""
  Horizon Cinemas
{user.get_branch().get_address()}
**booking receipt**

{booking.get_seat_type()} hall ticket     x{booking.get_number_of_seats()}\t{booking.get_price()}

booking reference : {booking.get_booking_reference()}


paid with card {payment.get_card_number()}

date: {booking.get_date_of_booking()}
user: {user}
Thank you!
"""
