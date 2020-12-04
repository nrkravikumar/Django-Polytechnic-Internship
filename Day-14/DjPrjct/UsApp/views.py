from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	# return HttpResponse("Hi Welcome User")
	return render(request,'sa/home.html')