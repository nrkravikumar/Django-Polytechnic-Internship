from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField()
	gender = models.CharField(max_length=10,choices=g)
