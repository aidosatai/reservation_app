from django.core.management.base import BaseCommand

from utils.tasks import (
    create_admin_user,
)


class Command(BaseCommand):
    help = "UPLOADING COMMON DATA to db"

    def handle(self, *args, **options):
        create_admin_user()
        print("\nSTATUS: All common data uploaded\n")
