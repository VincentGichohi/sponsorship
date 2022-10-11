from django.db import models
from credentials.models import CustomUser



class Staff(models.Model):
    course = models.ForeignKey()