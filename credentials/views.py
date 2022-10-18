from django.shortcuts import render, redirect, get_object_or_404
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import login, logout
