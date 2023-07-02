from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action

from rooms.models import Room
from rooms.serializers import (
    RoomAllFieldsSerializer,
    RoomListSerializer,
    SearchRoomSerializer
)


class RoomViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Room.objects.all()
    serializer_class = RoomAllFieldsSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['cost', 'number_of_beds']
    ordering_fields = ['cost', 'number_of_beds']
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'list':
            serializer_class = RoomListSerializer
        elif self.action == 'search_rooms':
            serializer_class = SearchRoomSerializer

        return serializer_class

    def get_permissions(self):
        permission_classes = self.permission_classes

        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]

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

    @action(detail=False, methods=['get'], url_path='search_rooms')
    def search_rooms(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.filter_available_rooms()
        page = self.paginate_queryset(instance)

        if page is not None and page:
            serializer = RoomListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RoomListSerializer(instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
