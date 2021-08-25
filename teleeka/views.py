from django.shortcuts import render, redirect 

from django.http import HttpResponse

from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login , logout 

from django.contrib.auth.decorators import login_required

from .decorators import unauthnticated_user, admin_only

from django.contrib.auth.models import Group

# Create your views here.

@unauthnticated_user
def reigsterPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='clients')

			user.groups.add(group)

			messages.success(request, 'Account was created for '+ username)
			return redirect('login')

	context = {'form':form}
	return render(request, 'teleeka/register.html', context)


# clients view
def clientPage(request):
	return render(request, 'teleeka/clients.html')

# Login View
@unauthnticated_user
def loginPage(request):

	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('home')

	else:
		messages.info(request, 'Username or Password is Incorrect')

	context = {}
	return render(request, 'teleeka/login.html',context)



# home view
@login_required(login_url='login')
@admin_only
def home(request):
	return render(request, 'teleeka/index.html')


# Logout View
@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

