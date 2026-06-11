from django.urls import path
from mypage import views

urlpatterns = [
    path("", views.home, name='home'),
    path("country/", views.country_details, name="country"),
    path("all_courses/", views.all_courses, name="courses"),



    path("login", views.login_page, name='login'),
    path("registration", views.register, name='registration'),
    path("logout", views.logout_page, name='logout'),

    path("profile", views.profile_page, name='profile'),
    path("update_profile", views.update_profile, name='update_profile'),
    path("delete_profile", views.delete_profile, name='delete_profile'),
    path('update-picture/',views.update_picture,name='update_picture'),
    path('delete-picture/',views.delete_picture,name='delete_picture'),




    path("my_courses/", views.course_list, name="my_courses"),
    path("section/<int:course_id>", views.section_list, name='section'),
    path("unit/<int:section_id>", views.unit_list, name='unit'),
    path('quiz/<int:unit_id>/', views.unit_quiz, name='quiz_page'),



]
