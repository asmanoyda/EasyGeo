from django.shortcuts import render
from users.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib import messages
from courses.models import Course, Section, Unit, Question
from mypage.models import User, Entrollment
from mypage.views import custom_login_required

# utils/decorators.py
from django.shortcuts import redirect
from functools import wraps



def all_courses(request):
    user = None

    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass

    query = request.GET.get('q', '')

    if query:
        courses = Course.objects.filter(
            course_name__istartswith=query,available=True
        ).order_by('course_name')
    else:
        courses = Course.objects.filter(available=True).order_by('course_name')

    return render(request, "all_courses.html", {
        'courses': courses,
        'user_data': user
    })


@custom_login_required
def course_list(request):
    # entrollment course list
    if request.session.get('user_id'):
        user = get_object_or_404(User, id=request.session['user_id'])

        # Get all enrollments for this user
        enrollments = Entrollment.objects.filter(user=user)

        # Get courses from those enrollments
        courses = [enrollment.course for enrollment in enrollments]

        context = {
            'courses': courses,
            'user_data': user
        }
        return render(request, 'course_list.html', context)

    return redirect('login')

@custom_login_required
def unit_quiz(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    questions = Question.objects.filter(unit=unit)

    return render(request, 'unit_quiz.html', {
        'unit': unit,
        'questions': questions
    })


@custom_login_required
def section_list(request, course_id):

    user = User.objects.get(id=request.session['user_id'])
    sections = Section.objects.filter(course_id=course_id)
    course = Course.objects.get(id=course_id)

    is_enrolled = Entrollment.objects.filter(course_id=course_id,user=user)
    flag = False
    if is_enrolled:
        flag=True

    context = {
        'sections': sections,
        'user_data': user,
        'course':course,
        "is_enrolled":flag
    }
    return render(request, 'section_list.html', context)


@custom_login_required
def unit_list(request, section_id):

    user = User.objects.get(id=request.session['user_id'])
    units = Unit.objects.filter(section_id=section_id)
    context = {
        'units': units,
        'user_data': user,
        'section_id': section_id
    }
    return render(request, 'unit_list.html', context)
