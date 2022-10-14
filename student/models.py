from django.db import models
from credentials.models import CustomUser


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
    staff = models.ForeignKey()