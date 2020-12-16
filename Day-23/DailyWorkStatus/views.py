from django.shortcuts import render
from django.http import HttpResponse
from DailyWorkStatus.forms import Usregis
from WorkLog import settings 
from django.core.mail import send_mail

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
				return HttpResponse("Mail Sent")
			return HttpResponse("Mail not sent")
			# print(p.username,p.email) to know the username and emailid
	y = Usregis()
	return render(request,'html/register.html',{'t':y})
