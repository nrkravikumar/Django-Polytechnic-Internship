from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def he(request):
	# print("Hello Welcome")
	return HttpResponse("Hi Welcome to Django Internship")

def hlp(req,n):
	return HttpResponse("Hi {} Welcome to Django Internship".format(n))