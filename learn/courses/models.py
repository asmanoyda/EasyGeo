from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.utils import timezone


def upload_image(instance, filename):
    course = slugify(instance.course_name)
    return f'courses/{course}/{filename}'


class Course(models.Model):
    course_name = models.CharField(max_length=245)
    image = models.ImageField(
        upload_to=upload_image,
        blank=True,
        null=True
    )
    description = models.TextField(default="")
    created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class Section(models.Model):
    section_name = models.CharField(max_length=245)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"{self.section_name }==>>{ str(self.course)}" 
    
    def return_name(self):
        return f"{self.section_name }" 


class Unit(models.Model):
    unit_name = models.CharField(max_length=245)
    quiz = models.CharField(max_length=245, blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=10000)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"{self.unit_name} ==> {str(self.section.return_name())} "


class Question(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
