from .serializers import MessageSerializer
from .models import Message
from rest_framework import viewsets
from .pagination import StandardResultsSetPagination
from rest_framework.permissions import (
    IsAuthenticated
)


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)
