from django.contrib import admin

# Register your models here.
from courses.models import Question,Course,Unit,Section


admin.site.register(Question)


from django.contrib import admin


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    # This makes the field read-only during both creation and editing
    list_display = ('unit_name','section','video', 'questions_count',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    # This makes the field read-only during both creation and editing
    list_display = ('section_name','unit_count','course')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','created','section_count')
    readonly_fields = ('created',)


