from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AdminRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']