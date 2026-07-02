from django.urls import path
from mypage import views
app_name = 'mypage' 

urlpatterns = [

    path("", views.home, name='home'),
    path("country/", views.country_details, name="country"),
     path("contact/", views.contact, name="contact_us"),
    path('create-entrollment/<int:course_id>/',
         views.create_entrollment, name='create_entrollment'),
    path('did-you-know/', views.did_you_know, name='did_you_know'),

]
