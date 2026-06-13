from django.urls import path
from users import views
app_name = 'users' 

urlpatterns = [
    
    
    path("login", views.login_page, name='login'),
    path("registration", views.register, name='registration'),
    path("logout", views.logout_page, name='logout'),

    path("profile", views.profile_page, name='profile'),
    path("update_profile", views.update_profile, name='update_profile'),
    path("delete_profile", views.delete_profile, name='delete_profile'),
    path('update-picture/',views.update_picture,name='update_picture'),
    path('delete-picture/',views.delete_picture,name='delete_picture'),







]