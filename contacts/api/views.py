from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contacts.models import Contact, Record

from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    Show all contacts and only new contacts after refresh.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def new_contacts(self, request, pk=None):
        user = self.get_object()
        obj, created = Record.objects.get_or_create(record_user=request.user)
        queryset = Contact.objects.filter(created_date__gt=obj.update)
        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        obj.save()
        return Response(serializer_data)
