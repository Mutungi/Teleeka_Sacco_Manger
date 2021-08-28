from django.shortcuts import render, redirect 

from django.http import HttpResponse

from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import CreateUserForm, CreateClientForm

from django.contrib.auth import authenticate, login , logout 

from django.contrib.auth.decorators import login_required

from .decorators import unauthnticated_user, admin_only

from django.contrib.auth.models import Group

from .models import *

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
	clients = Client.objects.all()
	client_count = clients.count()
	transactions = Transaction.objects.all()
	transaction_count = transactions.count()

	context = {'clients':clients, 'client_count':client_count,
				'transactions':transactions, 'transaction_count':transaction_count}


	return render(request, 'teleeka/index.html', context)


# Logout View
@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

def profile(request):
	return render(request, 'teleeka/profile.html')


def deposit(request, pk):

	return render(request, 'teleeka/deposit.html',context)


def withdrawl(request):
	return render(request, 'teleeka/withdrawl.html')



def transactions(request):
	clients = Client.objects.all()
	client_count = clients.count()
	transactions = Transaction.objects.all()
	transaction_count = transactions.count()

	context = {'clients':clients, 'client_count':client_count,
				'transactions':transactions, 'transaction_count':transaction_count}

	
	return render(request, 'teleeka/transactions.html', context)



def groupPage(request):
	return render(request, 'teleeka/groupPage.html')


# clients view
def clientPage(request):
	clients = Client.objects.all()
	client_count = clients.count()
	transactions = Transaction.objects.all()
	transaction_count = transactions.count()


	context = {'clients':clients, 'client_count':client_count,
				'transactions':transactions, 'transaction_count':transaction_count}

	return render(request, 'teleeka/clientspage.html', context)



def createClient(request):
	clients = Client.objects.all()
	client_count = clients.count()
	transactions = Transaction.objects.all()
	transaction_count = transactions.count()


	if request.method == 'POST':
		form = CreateClientForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				model = form.instance
				return redirect('clientpage')
			except:
				pass
	else:
		form = CreateClientForm()
	
	context = {'form':form,'clients':clients, 'client_count':client_count,
				'transactions':transactions, 'transaction_count':transaction_count}


	return render(request, 'teleeka/createClient.html',context)
				

def editClient(request,pk):
	# clients = Client.objects.all()
	client_edit = Client.objects.get(id=pk)
	form = CreateClientForm(instance=client_edit)
	# client_count = clients.count()
	# transactions = Transaction.objects.all()
	# transaction_count = transactions.count()

	if form.request.method == 'POST':
		form = CreateClientForm(request.POST, instance=client_edit)
		if form.is_valid():
			form.save()
			return redirect('clientpage')


	# if request.method == 'POST':
	# 	form = CreateClientForm(request.POST, instance=client)
	# 	if form.is_valid():
	# 		try:
	# 			form.save()
	# 			model = form.instance
	# 			return redirect('clientpage')
	# 		except:
	# 			pass
	# else:
	# 	form = CreateClientForm()
	
	context = {'form':form,'clients':clients, 'client_count':client_count,
				'transactions':transactions, 'transaction_count':transaction_count}


	return render(request, 'teleeka/editClient.html',context)
		



















