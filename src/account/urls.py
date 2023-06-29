from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.sing_in, name='sing_in'),
    path('register', views.sing_up, name='sing_up'),
    path('logout', views.log_out, name='log_out'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('update-password', views.update_password, name='update_password'),
]
