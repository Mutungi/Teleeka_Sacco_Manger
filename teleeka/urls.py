from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('register/', views.reigsterPage, name='register'),
	path('logout/', views.logoutUser, name='logout'),
	path('login/', views.loginPage, name='login'),
	path('clientpage/', views.clientPage, name='clientpage'),
	path('profile/', views.profile, name='profile'),
	path('deposit/', views.deposit, name='deposit'),
	path('withdrawl/', views.withdrawl, name='withdrawl'),
	path('transactions/', views.transactions, name='transactions'),
	path('groupPage/', views.groupPage, name='groupPage'),
	
	
	
	
	


]