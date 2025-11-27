from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Привычка """

    class Meta:
        model = Habit
        fields = ['id', 'title', 'video', 'owner']
