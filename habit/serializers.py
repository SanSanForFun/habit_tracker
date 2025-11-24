from rest_framework import serializers

from online.models import Course, Lesson
from online.validators import VideoValidator


class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Урок """

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video', 'owner']
        validators = [VideoValidator(field='video')]


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Курс """
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lessons.count()
