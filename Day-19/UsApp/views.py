from django.shortcuts import render,redirect
from django.http import HttpResponse
from UsApp.forms import UsReg,Updf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from DjPrjct import settings
from django.core.mail import send_mail
from django.contrib import messages

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
			messages.success(request,"User registered Successfully")
			return redirect('/lg')
	t = UsReg()
	return render(request,'sa/register.html',{'y':t})

@login_required
def dashboard(request):
	return render(request,'sa/dashboard.html')

@login_required
def mailsnd(request):
	pq = User.objects.values_list("email",flat=True)
	# print(pq)
	if request.method == "POST":
		# rec = request.POST['sndml'].split(",")
		# print(rec)
		rec = []
		adml = request.user.email
		rs = list(filter(None,pq))
		for m in rs:
			if m=="" or m==adml:
				continue
			else:
				rec.append(m)
		print(rec)
		sub = request.POST['subject']
		msg = request.POST['messg']
		sd = settings.EMAIL_HOST_USER
		t = send_mail(sub,msg,sd,rec)
		if t == 1:
			return redirect("/ml")
		return HttpResponse("Didnt send mail to particular person")
	return render(request,'sa/mailsending.html')

@login_required
def pfle(request):
	return render(request,'sa/profile.html')

@login_required
def updf(request):
	e = User.objects.get(id=request.user.id)
	if request.method == "POST":
		p = Updf(request.POST,instance=e)
		if p.is_valid():
			p.save()
			messages.info(request,'{} profile updated successfully'.format(request.user.username))
			return redirect('/pfl')
	p = Updf(instance=e)
	return render(request,'sa/upfle.html',{'h':p})