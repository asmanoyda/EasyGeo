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
from mypage.models import User, Entrollment, SectionEntrollment, UnitEntrollment
from users.views import custom_login_required
from courses.models import Course, Section, Unit
# utils/decorators.py
from django.shortcuts import redirect
from functools import wraps
import random


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
        section_enroll = SectionEntrollment.objects.create(
            section=section, entromment=abc)
        units = Unit.objects.filter(section_id=section.id)
        for unit in units:
            UnitEntrollment.objects.create(
                unit=unit, entromment=section_enroll, completed=False)

    return redirect("courses:get_enrollments")


def contact(request):
    user = None
    try:
        user = User.objects.get(id=request.session['user_id'])
    except:
        pass
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Message:", message)

        messages.success(request, "Your message has been sent successfully!")
    else:

        return render(request, "mypage/contact_us.html", {'user_data': user})


did_you_know_facts = [
    "💡 Russia spans 11 time zones.",
    "💡 Canada has more lakes than any other country.",
    "💡 Australia is wider than the Moon.",
    "💡 India is home to the wettest inhabited place on Earth, Mawsynram.",
    "💡 The Sahara Desert is larger than the entire United States (excluding Alaska).",
    "💡 Antarctica is the world's largest desert.",
    "💡 Japan consists of over 14,000 islands.",
    "💡 Brazil is the largest country in South America.",
    "💡 Nepal has eight of the world's ten highest mountains.",
    "💡 Vatican City is the smallest country in the world.",
    "💡 Indonesia has more than 17,000 islands.",
    "💡 Mongolia is the least densely populated country in the world.",
    "💡 Lake Baikal in Russia is the world's deepest freshwater lake.",
    "💡 Greenland is the world's largest island that is not a continent.",
    "💡 The Nile River flows through 11 countries.",
    "💡 Turkey is located on two continents: Europe and Asia.",
    "💡 France has the most time zones of any country.",
    "💡 Chile is over 4,300 km long but only about 175 km wide on average.",
    "💡 Iceland has no mosquitoes.",
    "💡 Bolivia has two capital cities: Sucre and La Paz."
]


def did_you_know(request):
    user = None
    try:
        user = User.objects.get(id=request.session['user_id'])
    except:
        pass

    fact = random.choice(did_you_know_facts)

    return render(request, "mypage/did_you_know.html", {
        "fact": fact,
        "user_data": user,
    })
