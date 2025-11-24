from django.urls import path
from online.views import CourseListView, LessonListView, LessonUpdateView, CourseUpdateView, LessonRetrieveView, \
    CourseRetrieveView, LessonDestroyView, LessonCreateView
from users.views import SubscribeCreateAPIView

app_name = 'online'

urlpatterns = [
    # Уроки
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_detail'),
    path('lessons/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),

    # Курсы
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseRetrieveView.as_view(), name='course_detail'),
    path('courses/update/<int:pk>/', CourseUpdateView.as_view(), name='course_update'),

    # Подписка
    path('subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe'),
]
