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
from mypage.models import User, Entrollment
from users.views import custom_login_required

# utils/decorators.py
from django.shortcuts import redirect
from functools import wraps


def home(request):
    user = None
    try:
        user = User.objects.get(id=request.session['user_id'])
    except:
        pass
    return render(request, "home.html", {'user_data': user})
   
@custom_login_required
def country_details(request):
    user = None
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    countries = Country.objects.all()
    return render(request, "country.html", {
        'user_data': user,
        'countries': countries
    })


@custom_login_required
def create_entrollment(request, course_id):
    abc = Entrollment.objects.create(
        user_id=request.session.get("user_id"),
        course_id=course_id
    )
    return redirect("courses:get_enrollments")
