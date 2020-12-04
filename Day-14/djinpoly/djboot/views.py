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
		w = UsForm(request.POST)
		if w.is_valid():
			w.save()
			return redirect('/displ')
	w = UsForm()
	return render(request,'djb/fstrg.html',{'ft':w})

def viewinfo(request,ty):
	m = Student.objects.get(id=ty)
	return render(request,'djb/vwinf.html',{'vi':m})

def upf(request,rq):
	n = Student.objects.get(id=rq)
	if request.method == "POST":
		a = UsForm(request.POST,instance=n)
		if a.is_valid():
			a.save()
			return redirect('/displ')
	a = UsForm(instance=n)
	return render(request,'djb/edpf.html',{'k':a})

def dlt(request,ze):
	c = Student.objects.get(id=ze)
	if request.method == "POST":
		c.delete()
		return redirect('/displ')
	return render(request,'djb/dltusr.html',{'fe':c})