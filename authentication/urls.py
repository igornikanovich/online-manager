from django.conf.urls import url, include
from django.urls import path

from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView

app_name = 'Authentication'

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]