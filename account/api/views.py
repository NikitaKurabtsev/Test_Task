from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import AccountSerializer, AccountDetailSerializer
from account.models import User


class OwnOrAdmin(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.user == obj:
            return True
        return False


class AccountAPI(APIView):

    def get(self, request):
        accounts = User.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        filter_backends = [SearchFilter]
        search_fields = ['gender']
        return Response(serializer.data)


class AccountDetailAPI(APIView):

    permission_classes = (OwnOrAdmin,)

    def get(self, request, username):
        account = User.objects.get(username=username)
        serializer = AccountDetailSerializer(account, context={"request": request})
        return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass