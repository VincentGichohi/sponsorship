from django.shortcuts import render
from django.views.generic.base import TemplateView

class Homepage(TemplateView):
    template_name = 'index.html'

class BaseTemplateView(TemplateView):
    template_name = 'base.html'

class Demo(TemplateView):
    template_name = 'student/student_register.html'