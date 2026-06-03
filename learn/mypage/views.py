from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime
from django.contrib import messages
from mypage.models import User, Course, Section, Unit, Question, Entrollment


def home(request):

    try:
        user = User.objects.get(id=request.session['user_id'])
        return render(request, "home.html", {'user_data': user})
    except:
        return render(request, "home.html", {})


def login_page(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            myuser = User.objects.get(username=username)
        except Exception as e:
            messages.error(request, 'username does not exits!')
            return redirect('login')
        if password == myuser.password:
            request.session["user_id"] = myuser.id
            messages.success(request, 'your account logged in sucesfully')
            return redirect('home')
        else:
            messages.error(request, 'password is in correct!')
            return redirect('login')


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    if request.method == "POST":
        name = request.POST['name']

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile_no = request.POST['mobile_no']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('registration')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('registration')
        if User.objects.filter(mobile_no=mobile_no).exists():
            messages.error(request, "mobile_no already exists!")
            return redirect('registration')
        user = User.objects.create(
            name=name,
            username=username,
            email=email,
            password=password,
            mobile_no=mobile_no
        )

        messages.success(request, "your account created succesfully")
        return redirect("login")


def course_list(request):
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


def logout_page(request):

    request.session.flush()
    messages.success(request, "your account logged out succesfully")

    return redirect("login")


def section_list(request, course_id):
    if request.session.get('user_id'):
        user = User.objects.get(id=request.session['user_id'])

        sections = Section.objects.filter(course_id=course_id)

        context = {
            'sections': sections,
            'user_data': user,
            'course_id': course_id,
        }

        return render(request, 'section_list.html', context)

    else:
        return redirect('login')


def unit_list(request, section_id):
    if request.session.get('user_id'):
        user = User.objects.get(id=request.session['user_id'])
        units = Unit.objects.filter(section_id=section_id)
        context = {
            'units': units,
            'user_data': user,
            'section_id': section_id
        }
        return render(request, 'unit_list.html', context)
    else:
        return redirect('login')


def profile_page(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect('login')

    user = User.objects.get(id=user_id)

    return render(request, "profile_page.html", {
        'user_data': user
    })


def delete_profile(request):
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    if not user_id:
        return redirect('login')
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        request.session.flush()

        user.delete()
        messages.success(
            request, "Your profile has been deleted successfully.")
        return redirect('login')
    else:
        return render(request, "delete_profile.html", {'user_data': user})


def update_profile(request):
    user_id = request.session.get("user_id")

    if not request.session.get('user_id'):
        return redirect('login')

    user = User.objects.get(id=user_id)

    if request.method == "GET":
        return render(request, "update_profile.html", {"user": user, 'user_data': user})

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.name = request.POST.get("name")

        user.email = request.POST.get("email")
        user.mobile_no = request.POST.get("mobile_no")
        user.save()
        messages.success(request, "Profile updated successfully")
        return redirect("profile")
    return render(request, "update_profile.html", {
        "user": user
    })


def delete_profile(request):
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    if not user_id:
        return redirect('login')
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        request.session.flush()

        user.delete()
        messages.success(
            request, "Your profile has been deleted successfully.")
        return redirect('login')
    else:
        return render(request, "delete_profile.html", {'user_data': user})


def unit_quiz(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    questions = Question.objects.filter(unit=unit)

    return render(request, 'unit_quiz.html', {
        'unit': unit,
        'questions': questions
    })

from django.shortcuts import render
from .models import User, Country

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