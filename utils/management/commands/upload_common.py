from django.core.management.base import BaseCommand
from django.core.management import call_command

from utils.tasks import (
    create_admin_user,
    create_common_user,
    create_rooms,
    create_bookings
)


class Command(BaseCommand):
    help = "UPLOADING COMMON DATA to db"

    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')
        call_command('collectstatic', '--noinput')
        create_admin_user()
        create_common_user()
        create_rooms()
        create_bookings()
        print("\nSTATUS: All common data uploaded\n")
