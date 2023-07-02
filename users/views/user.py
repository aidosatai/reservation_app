from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters import rest_framework as filters

from users.models import CustomUser
from users.serializers import (
    CustomUserAllFieldsSerializer,
    CustomUserCreateSerializer,
)


class CustomUserViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserAllFieldsSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'create':
            serializer_class = CustomUserCreateSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(data=self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
