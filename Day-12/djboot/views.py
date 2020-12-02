from django.shortcuts import render,redirect
from django.http import HttpResponse
from djboot.models import Student
from djboot.forms import UsForm

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
		return redirect('/displ')
	return render(request,'djb/stdrg.html')

def usd(request):
	y = Student.objects.all()
	return render(request,'djb/usrdisp.html',{'u':y})

def fusrg(request):
	if request.method == "POST":
		w = UsForm()
		if w.is_valid():
			return HttpResponse("Data Saved")
	w = UsForm()
	return render(request,'djb/fstrg.html',{'ft':w})