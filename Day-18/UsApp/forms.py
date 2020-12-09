from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ['username']
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Username",
			}),
		}