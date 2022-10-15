from django.db import models
from credentials.models import CustomUser, Staff, Course
from staff.models import *


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField(unique=True)
    birth_certificate = models.FileField(upload_to='images')
    national_id_file = models.FileField(upload_to='images')

    def __str__(self):
        return self.admin.last_name + " " + self.admin.first_name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LeaveReportStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    message = models.TextField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

