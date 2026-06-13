from django.db import models
from django.utils.text import slugify
from courses.models import Course
from users.models import User



class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.URLField()
    capital = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Entrollment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return str(self.course) + " ==>  "+str(self.user)
