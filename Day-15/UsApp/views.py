from django.shortcuts import render
from django.http import HttpResponse
from UsApp.forms import UsReg

# Create your views here.

def home(request):
	# return HttpResponse("Hi Welcome User")
	return render(request,'sa/home.html')

def abts(request):
	return render(request,'sa/about.html')

def cntc(request):
	return render(request,'sa/contact.html')

def regis(request):
	t = UsReg()
	return render(request,'sa/register.html',{'y':t})