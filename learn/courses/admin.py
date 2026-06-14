from django.contrib import admin

# Register your models here.
from courses.models import Question,Course,Unit,Section

admin.site.register(Section)

admin.site.register(Unit)

admin.site.register(Question)


from django.contrib import admin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # This makes the field read-only during both creation and editing
    readonly_fields = ('created',)



