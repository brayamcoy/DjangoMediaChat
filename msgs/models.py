from django.db import models
from django.contrib.auth.models import User
from room.models import Room


class Message(models.Model):
    image = models.ImageField(upload_to='assets/upload')
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
