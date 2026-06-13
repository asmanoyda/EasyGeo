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

    try:
        user = User.objects.get(id=request.session['user_id'])
        return render(request, "home.html", {'user_data': user})
    except:
        return render(request, "home.html", {})


def country_details(request):
    user = None

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass

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

    return redirect("my_courses")
