from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from habit.models import Habit
from habit.paginators import HabitPagination
from habit.models import Habit
from habit.serializers import HabitSerializer
from users.permissions import IsModerator, IsOwner


# Привычка
class HabitListView(generics.ListAPIView):
    """
    Просмотр списка всех привычек.
    Доступно всем пользователям.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPagination

    def get(self, request): # Для разбиения queryset на страницы
        queryset = Habit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class CourseCreateView(generics.CreateAPIView):
    """
    Создание привычки.
    Доступно авторизованным пользователям.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CourseRetrieveView(generics.RetrieveAPIView):
    """
    Просмотр деталей одной привычки.
    Доступно авторизованным пользователям.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class CourseUpdateView(generics.UpdateAPIView):
    """
    Редактирование привычки.
    Доступно только модераторам.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class CourseDestroyView(generics.DestroyAPIView):
    """
    Удаление привычки.
    Доступно только владельцам.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
