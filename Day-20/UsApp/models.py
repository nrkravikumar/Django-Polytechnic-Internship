from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class ImPfle(models.Model):
	u = models.OneToOneField(User,on_delete=models.CASCADE)
	im = models.ImageField(upload_to="Profile/",null=True,default="avatar.png")
	age = models.IntegerField(default=18) 

@receiver(post_save,sender=User)
def Crtpfle(sender,instance,created,**kwargs):
	if created:
		ImPfle.objects.create(u=instance)