from .serializers import MessageSerializer
from .models import Message
from rest_framework import viewsets


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer