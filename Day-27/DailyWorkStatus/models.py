from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	clg = [('AANM',"AANM & VVRSR Polytechnic - GDLR"),('SVGP',"S.V Govt Polytechnic"),('AANMR',"AANM & VVRSR Polytechnic - RJYD")]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	rollno = models.CharField(max_length=10)
	collegename = models.CharField(max_length=7,choices=clg)
	impf = models.ImageField(upload_to="Profile/",default="profile.jpeg") 

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)

class Worklog(models.Model):
	wks = [('yes','Completed'),('no','Not Completed')]
	date = models.DateField()
	description = models.TextField()
	workstatus = models.CharField(max_length=5,choices=wks)
	m = models.ForeignKey(User,on_delete=models.CASCADE)
