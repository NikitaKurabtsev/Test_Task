from copy import Error
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate 


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


class AuthenticateAPI(APIView):
    
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise Error
        if user is not None and user.check_password(password):
            return True
            
        