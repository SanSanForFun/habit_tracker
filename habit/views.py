from kombu.asynchronous.http import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from habit.models import Habit
from habit.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        if self.action == 'list':
            return Habit.objects.filter(user=self.request.user)
        return Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def public(self, request):
        habits = Habit.objects.filter(sign_of_publicity=True)
        page = self.paginate_queryset(habits)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(habits, many=True)
        return Response(serializer.data)
