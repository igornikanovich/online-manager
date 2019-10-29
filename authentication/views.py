from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class UserLoginAPIView(generics.CreateAPIView):
    """
    Endpoint for user authentication.
    """
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_200_OK, headers=headers)


class UserLogoutAPIView(APIView):
    """
    Endpoint for user logout.
    """
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
