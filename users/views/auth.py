from django.contrib.auth import logout
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.serializers import LoginSerializer, CustomUserAllFieldsSerializer
from utils.consts import CustomValidationError, ValidationErrorChoice
from utils.services import authenticate_user, delete_token


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = CustomUserAllFieldsSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'login':
            serializer_class = LoginSerializer

        return serializer_class

    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_agent = request.META.get("HTTP_USER_AGENT")

        user, token = authenticate_user(
            serializer.validated_data.get("phone"),
            serializer.validated_data.get("password"),
            user_agent,
        )

        response_data = dict()
        user_data = self.serializer_class(user, many=False).data
        response_data['access'] = token
        response_data['phone'] = user_data.get('phone')
        response_data['uuid'] = user_data.get('uuid')

        return Response(data=response_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=(IsAuthenticated,))
    def logout(self, request, **kwargs):
        """Сделает логаут и удаляет токен"""
        try:
            token = request.META.get("HTTP_AUTHORIZATION").split()[1]
            delete_token(request.user, token, request.data.get("all") is not None)
        except:
            raise CustomValidationError(ValidationErrorChoice.USER_TOKEN_NOT_FOUND.value)
        logout(request)
        return Response(data={'detail': 'Logout successfully! Token was deleted!'}, status=status.HTTP_200_OK)
