from django import forms
from django.forms.widgets import DateInput, TextInput
from .models import *


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Making changes
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomerUserForm(FormSettings):
    email = forms.EmailField(required=True)
