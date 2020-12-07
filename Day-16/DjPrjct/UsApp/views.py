from django.shortcuts import render
from django.http import HttpResponse
from UsApp.forms import UsReg
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	# return HttpResponse("Hi Welcome User")
	return render(request,'sa/home.html')

def abts(request):
	return render(request,'sa/about.html')

def cntc(request):
	return render(request,'sa/contact.html')

def regis(request):
	if request.method == "POST":
		t = UsReg(request.POST)
		if t.is_valid():
			t.save()
			
	t = UsReg()
	return render(request,'sa/register.html',{'y':t})