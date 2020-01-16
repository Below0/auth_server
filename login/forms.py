from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'pw')


class RegForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    pw = forms.CharField(max_length=15)
    re_pw = forms.CharField(max_length=15)
