from django.urls import path
from credentials.views import *
from . import views

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', views.account_login, name='login'),
]
