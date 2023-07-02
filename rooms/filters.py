from django_filters import rest_framework as filters

from rooms.models import Room


class RoomFilterSet(filters.FilterSet):
    type = filters.CharFilter(field_name='type', lookup_expr='exact', label='type')
    status = filters.CharFilter(field_name='status', lookup_expr='exact', label='status')

    class Meta:
        model = Room
        fields = 'cost', 'number_of_beds'
