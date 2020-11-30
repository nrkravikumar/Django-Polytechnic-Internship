from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200)
	rollno = models.CharField(max_length=200)
	branch = models.CharField(max_length=200)
	year = models.IntegerField()

	def __str__(self):
		return str(self.id) +" "+ self.name


