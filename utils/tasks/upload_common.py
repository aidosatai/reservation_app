from django.core.exceptions import ObjectDoesNotExist

from bookings.models import Booking
from rooms.models import Room
from users.models import CustomUser


def create_admin_user():
    try:
        user, created = CustomUser.objects.get_or_create(
            phone="+72223334455",
            first_name="Aidos",
            last_name="Atayev",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        if created or user is not None:
            user.set_password("1")
            user.save()
            print("Created admin user")
        else:
            print("ERROR: something went wrong, maybe admin already created?!")

            exit(1)
    except ObjectDoesNotExist:
        print("ERROR: something went wrong")

        exit(1)


def create_common_user():
    try:
        user, created = CustomUser.objects.get_or_create(
            phone="+71112223344",
            first_name="Michel",
            last_name="Jac",
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )

        if created or user is not None:
            user.set_password("1")
            user.save()
            print("Created common user")
        else:
            print("ERROR: something went wrong, maybe admin already created?!")

            exit(1)
    except ObjectDoesNotExist:
        print("ERROR: something went wrong")

        exit(1)


ROOM_DATA = [
    {
        "number": "101",
        "name": "Apartment Room",
        "description": "A cozy room with a queen-sized bed.",
        "kind": "apartment",
        "cost": 100,
        "number_of_beds": 1,
    },
    {
        "number": "102",
        "name": "Deluxe Room",
        "description": "A spacious room with two queen-sized beds.",
        "kind": "de_luxe",
        "cost": 150,
        "number_of_beds": 2,
    },
]


def create_rooms():
    for room_data in ROOM_DATA:
        room, created = Room.objects.get_or_create(**room_data)
        if created:
            print(f'Successfully created room "{room.name}" with ID {room.pk}')
        else:
            print(f'Room "{room.name}" already exists with ID {room.pk}')


BOOKING_DATA = [
    {
        "room_number": "101",
        "user_phone": "+71112223344",
        "status": "active",
        "start_date": "2023-08-01",
        "end_date": "2023-08-05",
    },
    {
        "room_number": "102",
        "user_phone": "+71112223344",
        "status": "active",
        "start_date": "2023-08-02",
        "end_date": "2023-08-06",
    },
]


def create_bookings():
    for booking_data in BOOKING_DATA:
        room_number = booking_data.pop("room_number")
        user_phone = booking_data.pop("user_phone")

        try:
            room = Room.objects.get(number=room_number)
            user = CustomUser.objects.get(email=user_phone)

            booking = Booking.objects.create(room=room, user=user, **booking_data)
            print(f'Successfully created booking with ID {booking.pk}')
        except Room.DoesNotExist:
            print(f'Error: Room with number {room_number} does not exist')
        except CustomUser.DoesNotExist:
            print(f'Error: User with email {user_phone} does not exist')
