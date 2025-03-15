from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/',views.Profile.as_view(),name="profile"),
    path('user-edit/',views.User_edit.as_view(),name="user-name")
    
    ]