from django import forms
from django.core.validators import MinLengthValidator

from .models import User


class UserForm(forms.ModelForm):
 
    password = forms.CharField(validators=[MinLengthValidator(8)])

    class Meta:
        model = User
        fields = ("username", "password")

