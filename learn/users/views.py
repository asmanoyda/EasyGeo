from django.shortcuts import render
from django.shortcuts import render
from users.models import User
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

from django.contrib import messages
from django.utils import timezone


def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.session.get('user_id'):
            return view_func(request, *args, **kwargs)

        return redirect('users:login')
    return wrapper


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
            return redirect('users:login')
        if password == myuser.password:
            request.session["user_id"] = myuser.id
            messages.success(request, 'your account logged in sucesfully')
            return redirect('mypage:home')
        else:
            messages.error(request, 'password is in correct!')
            return redirect('users:login')


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


@custom_login_required
def logout_page(request):

    request.session.flush()
    messages.success(request, "your account logged out succesfully")
    return redirect("users:login")


@custom_login_required
def update_picture(request):

    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
            user.last_updated = timezone.now()
            user.save()

    return redirect("users:profile_view")


@custom_login_required
def delete_picture(request):

    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        if user.profile_picture:
            user.profile_picture.delete()
            user.profile_picture = None
            user.last_updated = timezone.now()
            user.save()

    return redirect("users:profile_view")


@custom_login_required
def profile_page(request):

    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)
    return render(
        request,
        "profile_page.html",
        {"user_data": user}
    )


@custom_login_required
def delete_profile(request):
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        request.session.flush()
        user.delete()
        messages.success(
            request, "Your profile has been deleted successfully.")
        return redirect('users:login')
    else:
        return render(request, "delete_profile.html", {'user_data': user})


@custom_login_required
def update_profile(request):
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    if request.method == "GET":
        return render(request, "update_profile.html", {"user": user, 'user_data': user})

    if request.method == "POST":
        user.last_updated = timezone.now()
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.mobile_no = request.POST.get("mobile_no")
        user.name = request.POST.get("name")
        user.save()
        messages.success(request, "Profile updated successfully")
        return redirect("users:profile_view")
    
    return render(request, "update_profile.html", {"user": user})
