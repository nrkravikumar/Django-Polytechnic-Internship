from django.shortcuts import render
from django.http import HttpResponse
from djboot.models import Student

# Create your views here.

def home(request):
	return render(request,'djb/home.html')

def strg(request):
	if request.method == "POST":
		nm = request.POST['n']
		rll = request.POST['rl']
		bnch = request.POST['brc']
		yer = request.POST['yr']
		t = Student(name=nm,rollno=rll,branch=bnch,year=str(yer))
		t.save()
		return HttpResponse("{} Record Saved Successfully".format(t.name))
	return render(request,'djb/stdrg.html')