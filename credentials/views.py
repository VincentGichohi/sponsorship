from django.shortcuts import render, redirect, get_object_or_404, reverse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
import requests


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






