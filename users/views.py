from django.contrib.auth.views import LoginView, LogoutView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserLoginAPIView(LoginView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLogoutAPIView(LogoutView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
