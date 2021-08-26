from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('register/', views.reigsterPage, name='register'),
	path('logout/', views.logoutUser, name='logout'),
	path('login/', views.loginPage, name='login'),
	path('client/', views.clientPage, name='client'),
	path('profile/', views.profile, name='profile'),
	
	
	


]