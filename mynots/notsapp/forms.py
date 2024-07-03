from django import forms
from .models import *

class signupfrom(forms.ModelForm):
    class Meta:
        model=newuser
        fields='__all__'