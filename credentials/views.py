from django.shortcuts import render, redirect, get_object_or_404, reverse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json


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
    return render(request, 'student/student_register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("admin_home"))
        if request.user.user_type == '2':
            return redirect(reverse('staff_home'))
        else:
            return redirect(reverse('student_home'))
    return render(request, 'credentials/login.html')


def account_login(request, **kwargs):
    if request.method != "POST":
        return HttpResponse("<h4>Denied.</h4>")
    else:
        # Google Recaptcha
        captcha_token = request.POST.get('g-recaptcha-response')
        captcha_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_key = "6LdjyoUiAAAAAIIcvaVbfuNTB88Aqza0uFwTpI57"
        data = {
            'secret': captcha_key,
            'response': captcha_token
        }
        # Make a request
        try:
            captcha_server = requests.post(url=captcha_url, data=data)
            response = json.loads(captcha_server.text)
            if not response['success']:  # replaced response['success'] == False
                messages.error(request, 'Invalid captcha. Try again.')
                return redirect('/')
        except:
            messages.error(request, 'Captcha could not be verified. Try again.')
            return redirect('/')

        # Authenticate
        user = EmailBackend.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse('admin_home'))
            elif user.user_type == '2':
                return redirect(reverse('staff_home'))
        else:
            messages.error(request, 'Invalid details')
            return redirect('/')


def logout_user(request):
    if request.user is not None:
        logout(request)
    return redirect('/')
