from django.shortcuts import render
from credentials.forms import RegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from credentials.models import MyUser
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(SuccessMessageMixin, CreateView):
    template_name = 'student/student_register.html'
    success_url = reverse_lazy('student/login')
    form_class = RegisterForm
    success_message = "Your account has been created successfully."
