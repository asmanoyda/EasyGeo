from django.urls import path
from courses import views
app_name = 'courses' 

urlpatterns = [

    path("all-courses/", views.all_courses, name="all_courses"),
    path("get-enrollments/", views.get_enrollments, name="get_enrollments"),
    path("get-section/<int:course_id>", views.section_list, name='section'),
    path("unit/<int:section_id>/<int:course_id>", views.unit_list, name='unit'),    
    path('quiz/<int:unit_id>/', views.unit_quiz, name='quiz_page'),


]


# get-ENTROMENT_LIST //ALL
# CREATE-ENTROMENT //
# UDPATE-ENTROMENT //ID
# DELETET- 
# VIEW-ENTROMENT/ID ID