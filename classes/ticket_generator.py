class Ticket_generator():
    def gen_ticket(booking, cinema):
        show = booking.get_show()
        listing = show.get_listing()
        film = listing.get_film()
        return f"""
Horizon Cinemas

film: {film}
duration: {film.get_duration()}
age rating: {film.get_age_rating()}

date and time: {listing.get_date()} {show.get_time()}

cinema: {cinema.get_address()}
{show.get_screen()}

price: {booking.get_price()}
seat type: {booking.get_seat_type()}
booking reference : {booking.get_booking_reference()}
date booked: {booking.get_date_of_booking()}


Thank you!
"""
