from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action

from bookings.models import Booking
from bookings.serializers import (
    BookingAllFieldsSerializer,
    BookingCreateSerializer,
    BookingListSerializer,
    BookingCancelSerializer
)


class BookingViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = Booking.objects.all()
    serializer_class = BookingAllFieldsSerializer

    permission_classes = [AllowAny]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'list' or self.action == 'my_booking':
            serializer_class = BookingListSerializer
        elif self.action == 'create':
            serializer_class = BookingCreateSerializer
        elif self.action == 'cancel_booking':
            serializer_class = BookingCancelSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = self.permission_classes

        if self.action == 'create' or \
                self.action == 'retrieve' or \
                self.action == 'list' or \
                self.action == 'cancel_booking':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset.all())
        page = self.paginate_queryset(queryset)

        if page is not None and page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(data=self.serializer_class(instance).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'], url_path='cancel_booking')
    def cancel_booking(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.cancel_booking():
            return Response(data={"detail": 'Booking canceled successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response(data={"detail": 'Something gone wrong! Try again, pls!'},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='my_booking')
    def my_booking(self, request, *args, **kwargs):
        instance = self.queryset.filter(user=request.user)
        page = self.paginate_queryset(instance)

        if page is not None and page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
