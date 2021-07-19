from django.db.models import fields
from rest_framework import serializers

from account.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'gender')
