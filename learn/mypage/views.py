from django.shortcuts import render
from .models import User, Country
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib import messages
from mypage.models import User, Entrollment, SectionEntrollment,UnitEntrollment
from users.views import custom_login_required
from courses.models import Course,Section, Unit
# utils/decorators.py
from django.shortcuts import redirect
from functools import wraps



def home(request):
    user = None
    try:
        user = User.objects.get(id=request.session['user_id'])
    except:
        pass
    return render(request, "mypage/home.html", {'user_data': user})
   
@custom_login_required
def country_details(request):
    user = None
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    countries = Country.objects.all()
    return render(request, "mypage/country.html", {
        'user_data': user,
        'countries': countries
    })


@custom_login_required
def create_entrollment(request, course_id):
    abc = Entrollment.objects.create(
        user_id=request.session.get("user_id"),
        course_id=course_id
    )
    sections = Section.objects.filter(course_id=course_id)
    for section in sections:
        section_enroll = SectionEntrollment.objects.create(section=section, entromment=abc)
        units =Unit.objects.filter(section_id=section.id)

        for unit in units:

            UnitEntrollment.objects.create(unit=unit,entromment=section_enroll,completed= False)

    return redirect("courses:get_enrollments")


