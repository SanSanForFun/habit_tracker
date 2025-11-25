from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, SubscribeCreateAPIView, PaymentsCreateAPIView, UserLoginAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny)), name='token_refresh'),
    path('subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe'),
    path('payment/', PaymentsCreateAPIView.as_view(), name='payment')
]
