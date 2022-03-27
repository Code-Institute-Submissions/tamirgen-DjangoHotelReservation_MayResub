from booking.models import Booking, Room


def book_room(request, room, check_in, check_out):
    # This function makes a Booking object and saves it
    booking = Booking.objects.create(
        user=request.user,
        room=room,
        check_in=check_in,
        check_out=check_out,
    )
    booking.save()

    return booking
