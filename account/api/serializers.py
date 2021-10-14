from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import User, Contact


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'gender')


class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ('is_sent', 'new_contact')
