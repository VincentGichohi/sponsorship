from django.db import models

import credentials.models
from credentials.models import *


class Staff(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user')
