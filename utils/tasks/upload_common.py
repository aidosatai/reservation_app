from django.core.exceptions import ObjectDoesNotExist

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
        else:
            print("ERROR: something went wrong, maybe admin already created?!")

            exit(1)
    except ObjectDoesNotExist:
        print("ERROR: something went wrong")

        exit(1)