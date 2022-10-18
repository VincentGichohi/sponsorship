from django.shortcuts import render, redirect, get_object_or_404
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import login, logout


def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    context = {
        'userForm': userForm,
    }
    if request.method == 'POST':
        if userForm.is_valid():

