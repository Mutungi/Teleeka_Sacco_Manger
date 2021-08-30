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
		fields = ['fullname', 'email','phone','group','status']
	
class CreateDepositForm(ModelForm):
	class Meta:
		model = Deposit 
		fields = '__all__'




class CreateWithdrawlForm(ModelForm):
	class Meta:
		model = Withdrawl 
		fields = '__all__'

class CreateSavingGroupForm(ModelForm):
	class Meta:
		model = SavingGroup 
		fields = '__all__'


