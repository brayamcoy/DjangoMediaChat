from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
