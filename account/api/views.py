from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter


from .serializers import AccountSerializer, AccountDetailSerializer
from account.models import User


class AccountAPI(APIView):

    def get(self, request):
        accounts = User.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        filter_backends = [SearchFilter]
        search_fields = ['gender']
        return Response(serializer.data)


class AccountDetailAPI(APIView):

    def get(self, request, username):
        account = User.objects.get(username=request.user)
        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)
