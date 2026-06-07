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
from mypage.models import User, Course, Section, Unit, Question, Entrollment


# utils/decorators.py
from django.shortcuts import redirect
from functools import wraps


def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.session.get('user_id'):
            return view_func(request, *args, **kwargs)

        return redirect('login')
    return wrapper


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


def all_courses(request):
    courses = Course.objects.all()
    user = None

    user_id = request.session.get('user_id')

    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass

    return render(request, "all_courses.html", {
        'courses': courses,
        'user_data': user
    })

@custom_login_required
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


@custom_login_required
def logout_page(request):

    request.session.flush()
    messages.success(request, "your account logged out succesfully")
    return redirect("login")


@custom_login_required
def section_list(request, course_id):

    user = User.objects.get(id=request.session['user_id'])
    sections = Section.objects.filter(course_id=course_id)
    context = {
        'sections': sections,
        'user_data': user,
        'course_id': course_id,
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

@custom_login_required
def profile_page(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("login")

    user_data = User.objects.get(id=user_id)

    return render(
        request,
        "profile_page.html",
        {"user_data": user_data}
    )

@custom_login_required
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

@custom_login_required
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

@custom_login_required
def unit_quiz(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    questions = Question.objects.filter(unit=unit)

    return render(request, 'unit_quiz.html', {
        'unit': unit,
        'questions': questions
    })


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
def update_picture(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("login")

    try:
        user = User.objects.get(id=user_id)

        if request.method == "POST":
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
                user.save()

    except User.DoesNotExist:
        return redirect("login")

    return redirect("profile")

@custom_login_required
def delete_picture(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("login")

    try:
        user = User.objects.get(id=user_id)

        if request.method == "POST":
            if user.profile_picture:
                user.profile_picture.delete()
                user.profile_picture = None
                user.save()

    except User.DoesNotExist:
        return redirect("login")

    return redirect("profile")
