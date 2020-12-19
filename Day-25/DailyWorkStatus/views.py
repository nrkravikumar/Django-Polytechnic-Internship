from django.shortcuts import render,redirect
from django.http import HttpResponse
from DailyWorkStatus.forms import Usregis,Upd,Pad
from WorkLog import settings 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from DailyWorkStatus.models import Exfd


# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			print(rc)
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or username or password")
			# print(p.username,p.email)
	y = Usregis()
	return render(request,'html/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def prfle(request):
	return render(request,'html/profile.html')

@login_required
def updf(request):
	y = User.objects.get(id=request.user.id)
	m = y.id
	print(m)
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			er = p.save(commit=False)
			r = t.save(commit=False)
			r.d_id = er.id
			er.save()
			r.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'html/updateprofile.html',{'r':p,'q':t})