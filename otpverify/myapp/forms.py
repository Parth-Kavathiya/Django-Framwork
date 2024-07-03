from django import forms
from .models import *
# create forms
class user_signup(forms.ModelForm):
    class Meta:
        model=user
        fields='__all__'