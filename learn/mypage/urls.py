from django.urls import path
from mypage import views

urlpatterns = [
    path("", views.home, name='home'),
    path("country/", views.country_details, name="country"),
    path('create-entrollment/<int:course_id>/',
         views.create_entrollment, name='create_entrollment'),


]
