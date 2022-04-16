from django.urls import path
# from student.views import homepage
from student.views import Homepage

urlpatterns = [
   path('home/', Homepage.as_view(), name='homepage'),
]
