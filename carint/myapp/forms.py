from django import forms
from .models import *


class user(forms.ModelForm):
    class Meta:
        model=newUser
        fields='__all__'