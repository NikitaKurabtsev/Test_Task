from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


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


# class AccountDetailAPI(APIView):
#
#     def get(self, request, username):
#         if request.user.is_authenticated and request.user.is_superuser:
#             account = User.objects.get(username=username)
#             serializer = AccountDetailSerializer(account, context={"request": request})
#             return Response(serializer.data)
#         elif request.user.is_authenticated and request.user.username == username:
#             serializer = AccountDetailSerializer(request.user, context={"request": request})
#             return Response(serializer.data)
#         else:
#             raise exceptions.NotAuthenticated()
