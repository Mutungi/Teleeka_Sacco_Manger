from django.shortcuts import render, redirect 

from django.http import HttpResponse

# Create your views here.


def register(request):
	return render(request, 'teleeka/register.html')


def loginPage(request):
	return render(request, 'teleeka/login.html')




def home(request):
	return render(request, 'teleeka/index.html')


