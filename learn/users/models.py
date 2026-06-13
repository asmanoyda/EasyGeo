from django.db import models


class User(models.Model):
    name = models.CharField(max_length=233)
    username = models.CharField(max_length=100, unique=True)
    mobile_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True)

    def __str__(self):
        return self.username



