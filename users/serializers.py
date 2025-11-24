from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import Payments, User, Subscribe


class PaymentsSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Платежи """

    class Meta:
        model = Payments
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
