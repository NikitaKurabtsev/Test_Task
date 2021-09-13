from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import User


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'gender')


class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
