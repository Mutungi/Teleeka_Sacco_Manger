from django.forms import ModelForm

from django import forms 

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1', 'password2']


class CreateClientForm(ModelForm):
	class Meta:
		model = Client 
		fields = ['fullname', 'email','phone','group','status' ]
	






