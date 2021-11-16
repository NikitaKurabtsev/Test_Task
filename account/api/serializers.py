from rest_framework import serializers

from account.models import User


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'gender')


class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
