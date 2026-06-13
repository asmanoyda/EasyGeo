from django.urls import path
from courses import views

urlpatterns = [

    path("all_courses/", views.all_courses, name="courses"),
    path("my_courses/", views.course_list, name="my_courses"),
    path("course/<int:course_id>", views.section_list, name='section'),
    path("unit/<int:section_id>", views.unit_list, name='unit'),
    path('quiz/<int:unit_id>/', views.unit_quiz, name='quiz_page'),


]