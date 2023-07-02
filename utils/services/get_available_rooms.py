from bookings.models import Booking
from rooms.models import Room
from utils.consts.rooms import BookStatusChoice


def get_available_rooms(start_date: str, end_date: str):
    booked_rooms = Booking.objects.filter(
        start_date__lte=end_date,
        end_date__gte=start_date,
        status=BookStatusChoice.ACTIVE.value
    ).values_list('room_id', flat=True)

    available_rooms = Room.objects.exclude(uuid__in=booked_rooms)
    return available_rooms


def get_not_available_rooms(start_date: str, end_date: str):
    booked_rooms = Booking.objects.filter(
        start_date__lte=end_date,
        end_date__gte=start_date,
        status=BookStatusChoice.ACTIVE.value
    ).values_list('room_id', flat=True)

    not_available_rooms = Room.objects.filter(uuid__in=booked_rooms)
    return not_available_rooms
