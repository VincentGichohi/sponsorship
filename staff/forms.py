from django import forms

from credentials.forms import CustomUserForm
from . import models
from credentials.models import *
from credentials.forms import *


class StaffForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)

    class Meta(CustomUserForm.Meta):
        model = Staff
        fields = CustomUserForm.Meta.fields + ['course']



class CourseForm(FormSettings):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Course
        fields = ['name']


