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

# class CreateClientForm(forms.Form):

# 	 fullname = forms.CharField(
#         widget=forms.TextInput(
#             attrs={                
#                 "class": "form-control"
#             }
#         ))
# 	 email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={                
#                 "class": "form-control"
#             }
#         ))
# 	 phone = forms.CharField(
#         widget=forms.TextInput(
#             attrs={                
#                 "class": "form-control"
#             }
#         ))
# 	 group = forms.CharField(
#         widget=forms.TextInput(
#             attrs={                
#                 "class": "form-control"
#             }
#         ))
# 	 status = forms.CharField(
#         widget=forms.TextInput(
#             # attrs={                
#             #     "class": "form-control"
#             # }
#         ))
# 	 class Meta:
# 	 	model = Client
# 	 	fields = ('fullname','email','phone','group','status')
	# class Meta:
	# 	model = Client 
	# 	fields = ('fullname','email','phone','group','status')