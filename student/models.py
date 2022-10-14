from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField(unique=True)
    birth_certificate = models.FileField(upload_to='images')
    national_id_file = models.FileField(upload_to='images')
