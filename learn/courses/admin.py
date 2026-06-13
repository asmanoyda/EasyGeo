from django.contrib import admin

# Register your models here.
from courses.models import Question,Course,Unit,Section

admin.site.register(Course)
admin.site.register(Section)

admin.site.register(Unit)

admin.site.register(Question)

