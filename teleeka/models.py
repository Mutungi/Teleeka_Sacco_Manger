from django.db import models

# Create your models here.

class Client(models.Model):
	STATUS = (
		('Active','Active'),
		('Pending', 'Pending'),
		)
	GROUPS = (
		('Jinja-Youth','Jinja-Youth'),
		('Kampala-Youth', 'Kampala-Youth'),
		('Entebbe-Youth', 'Entebbe-Youth'),
		('Mbale-Youth', 'Mable-Youth'),
		('Gulu-Youth', 'Gulu-Youth'),
		('Arua-Youth', 'Arua-Youth'),
		)
	fullname = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	group = models.CharField(max_length=200, null=True, choices=GROUPS)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=200, null=True)



	def __str__(self):
		return self.fullname



class Group(models.Model):
	STATUS = (
		('Verified','Verified'),
		('Pending-verification', 'Pending-verification'),
		)
	groupName = models.CharField(max_length=200, null=True)
	groupNumber = models.IntegerField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return self.groupName


class Transaction(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Completed', 'Completed'),
		)
	clientName = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
	amount = models.IntegerField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return str(self.clientName)






