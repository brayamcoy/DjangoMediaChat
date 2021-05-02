from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='assets/upload')
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
