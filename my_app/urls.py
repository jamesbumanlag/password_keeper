from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user, name='login'),
    path('home',views.home, name='home'),
    path('login',views.login_user, name='login'),
    path('register',views.register, name='register'),
    path('reset',views.reset, name='reset'),
    path('logout',views.logout_user, name='logout'),
]