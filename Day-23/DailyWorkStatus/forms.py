from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Usregis(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]
		widgets = {
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your First Name",
			"required":True,
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		}