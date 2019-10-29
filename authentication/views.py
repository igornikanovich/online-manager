from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, status, authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher, Student
from .serializers import UserRegisterSerializer, StudentSerializer, TeacherSerializer, UserLoginSerializer


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


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
