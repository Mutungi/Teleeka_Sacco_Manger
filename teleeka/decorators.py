
from django.http import HttpResponse

from django.shortcuts import redirect


def unauthnticated_user(view_func):
	def wrapper_func(request, *args, **kwarags):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwarags)

	return wrapper_func


def admin_only(view_func):
	def wrapper_function(request, *args, **kwarags):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'clients':
			return redirect('client')

		if group == 'admin':
			return view_func(request, *args, **kwarags)

	return wrapper_function