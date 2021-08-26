from django.db import models

# Create your models here.

class Client(models.Model):
	fullname = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	group = models.CharField(max_length=200, null=True)
	balance = models.IntegerField(max_length=200, null=True)


	def __str__(self):
		return self.fullname



class Deposit(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Completed', 'Completed'),
		)
	fullname = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	group = models.CharField(max_length=200, null=True)
	amount_to_deposit = models.IntegerField(max_length=200, null=True)
	balance = models.IntegerField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.fullname


class Withdrwal(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Completed', 'Completed'),
		)
	fullname = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	group = models.CharField(max_length=200, null=True)
	amount_to_deposit = models.IntegerField(max_length=200, null=True)
	balance = models.IntegerField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.fullname


class Group(models.Model):
	groupName = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.groupName







