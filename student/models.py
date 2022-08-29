from django.db import models
from credentials.models import *


class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50, blank=False)
    birth_certificate = models.ImageField(blank=False)
    national_id = models.ImageField(blank=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        return self.first_name + " " + self.last_name


class School(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, default=False)
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=50)
    academic_level = models.CharField(max_length=30)
    expected_year_of_completion = models.DateTimeField(auto_now_add=True)

    def __init__(self):
        return self.school_name


