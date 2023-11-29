from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(),

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile=Profile(user=instance)
            user_profile.save()