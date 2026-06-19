from django.db import models
from django.utils.text import slugify
from courses.models import Course
from users.models import User
from courses.models import Section,Unit



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
        null=True,
    
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    def get_progress(self):
        enrollment = sum (1 for i in self.section_entrollment.filter() if i.get_progress()==100)
        count = self.course.section_count()
        progress = (enrollment/count)*100
        return progress 

    def __str__(self):
        return str(self.course) + " ==>  "+str(self.user)
    class Meta:
        unique_together = [('user', 'course')]


class SectionEntrollment(models.Model):
    entromment = models.ForeignKey(
        Entrollment,
        on_delete=models.CASCADE,
        null=True,
        related_name="section_entrollment"
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=True
    )
    def get_progress(self):
        
        enrollment = sum (1 for i in self.unit_entrollment.filter(completed=True))
        count = self.section.unit_count()
        progress = (enrollment/count)*100
        return progress 


    def __str__(self):
        return str(self.section) + " ==>  "+str(self.entromment)
    class Meta:
        unique_together = [('section', 'entromment')]
    

class UnitEntrollment(models.Model):
    entromment = models.ForeignKey(
        SectionEntrollment,
        on_delete=models.CASCADE,
        null=True,
        related_name='unit_entrollment',
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return str(self.unit) + " ==>  "+str(self.entromment)

    completed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = [('unit', 'entromment')]
