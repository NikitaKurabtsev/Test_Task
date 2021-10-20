import http
from copy import Error
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate 


from .serializers import AccountSerializer, AccountDetailSerializer, ContactSerializer
from account.models import User, Contact


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
            

class GetContactAPI(APIView):

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class GetNewContactAPI(APIView):

    def get(self, request):
        contacts = Contact.objects.filter(new_contact=True)
        serializer = ContactSerializer(contacts, many=True)

        def post_processing_refresh():
            for contact in contacts:
                contact.new_contact = False
                contact.save()

        return Response(serializer.data, post_processing_refresh())
