from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import user 

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = user
        fields = ['username', 'email']