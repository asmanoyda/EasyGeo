from django.contrib import admin

from mypage.models import Entrollment, Country, UnitEntrollment, SectionEntrollment, DidYouKnowFact

admin.site.register(Country)

admin.site.register(UnitEntrollment)



@admin.register(SectionEntrollment)
class SectionEntrollmentAdmin(admin.ModelAdmin):
    
    list_display = ('get_progress','section','entromment')

@admin.register(Entrollment)
class CourseEntrollmentAdmin(admin.ModelAdmin):
    
    list_display = ('get_progress','entrollment_date','course','user')

@admin.register(DidYouKnowFact)
class DidYouKnowFactAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")    

