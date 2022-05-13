from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

class Homepage(TemplateView):
    template_name = 'index.html'

class BaseTemplateView(TemplateView):
    template_name = 'base.html'

class Demo(CreateView):
    template_name = 'student/student_register.html'