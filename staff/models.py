from django.db import models
from credentials.models import CustomUser



class Staff(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
