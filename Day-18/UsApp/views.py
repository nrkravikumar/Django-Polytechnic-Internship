from django.shortcuts import render,redirect
from django.http import HttpResponse
from UsApp.forms import UsReg
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from DjPrjct import settings
from django.core.mail import send_mail

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
			return redirect('/lg')
	t = UsReg()
	return render(request,'sa/register.html',{'y':t})

@login_required
def dashboard(request):
	return render(request,'sa/dashboard.html')

@login_required
def mailsnd(request):
	if request.method == "POST":
		rec = request.POST['sndml']
		sub = request.POST['subject']
		msg = request.POST['messg']
		sd = settings.EMAIL_HOST_USER
		t = send_mail(sub,msg,sd,[rec])
		if t == 1:
			return redirect("/ml")
		return HttpResponse("Didnt send mail to particular person")
	return render(request,'sa/mailsending.html')