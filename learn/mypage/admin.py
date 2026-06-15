from django.contrib import admin

from mypage.models import  Entrollment, Country, UnitEntrollment,SectionEntrollment

admin.site.register(Entrollment)
admin.site.register(Country)


admin.site.register(UnitEntrollment)
admin.site.register(SectionEntrollment)
