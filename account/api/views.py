from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AccountSerializer
from account.models import User


class AccountAPI(APIView):

    def get(self, request):
        accounts = User.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
