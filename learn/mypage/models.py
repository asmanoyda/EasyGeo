from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.URLField()   
    capital = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=233)
    username = models.CharField(max_length=100, unique=True)
    mobile_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Course(models.Model):
    course_name = models.CharField(max_length=245)
    image = models.CharField(max_length=100, blank=True, null=True)  

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
        return self.section_name
    
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
        return self.unit_name

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



