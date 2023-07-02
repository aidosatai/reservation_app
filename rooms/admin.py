from django.contrib import admin

from rooms.models import Room
from bookings.models import Booking

admin.site.register(Booking)


class BookingRoomAdminInline(admin.StackedInline):
    model = Booking
    extra = 0
    classes = ['collapse']


@admin.register(Room)
class ProductAdmin(admin.ModelAdmin):
    model = Room
    readonly_fields = ['uuid']
    inlines = [BookingRoomAdminInline]
    list_display = ['name', 'number', 'kind']
    fieldsets = (
            (
                'Main', {
                    'fields': ('uuid', 'number', 'name',)
                }
            ),
            (
                'Additional information', {
                    'fields': ('description', 'kind', 'cost', 'number_of_beds')
                }
            )
        )
