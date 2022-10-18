from django.shortcuts import render, redirect, get_object_or_404, reverse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect


def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    context = {
        'userForm': userForm,
    }
    if request.method == 'POST':
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.save()
            messages.success(request, 'Account created. You can proceed to login.')
            return redirect(reverse('account_login'))
        else:
            messages.error(request, "Provided data field validation failed.")
        return render(request, 'registration.html')


def doLogin(request, **kwargs):
    if request.method != "POST":
        return HttpResponse()


