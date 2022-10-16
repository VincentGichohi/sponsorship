from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(CustomUser, UserModel)
admin.site.register(Session)
