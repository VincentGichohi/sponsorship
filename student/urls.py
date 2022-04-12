from django.urls import path
# from student.views import homepage
from . import views

urlpatterns = [
   path('home/', views.homepage, name='homepage'),
]