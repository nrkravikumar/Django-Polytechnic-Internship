from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def he(request):
	# print("Hello Welcome")
	return HttpResponse("Hi Welcome to Django Internship")

def hlp(req,n):
	return HttpResponse("Hi {} Welcome to Django Internship".format(n))

def tble(request,t):
	# print(t,type(t))
	y = []
	for p in range(1,11):
		# print("{} x {:02} = {:02}".format(t,p,t*p))
		u = "{} x {:02} = {:02}".format(t,p,t*p)+"<br/>"
		y.append(u)
	# print(y)
	return HttpResponse(y)

def record(request,age,name,sal=2300):
	return HttpResponse("Hi Your name is: {}<br/>Your age is: {}<br/> Your salary is: {}".format(name,age,str(sal)))
	# m = "Hi your name is: {}<br/>Your age is: {}<br/>".format(name,age)
	# p = "Your sal is: "+str(sal)
	# return HttpResponse(m+p)

def stdnt(request,prc,name,age):
	t = "<h5 style='background-color:green;color:white;font-size:20px'>Hi Welcome {}</h5>".format(name)
	u = "<h4>Your age is: {}</h4>".format(age)
	return HttpResponse(t+u+"<script>alert('Hi')</script>")

def rcde(request,name,a):
	return HttpResponse("<h3 style='margin-left:30%;background-color:yellow;margin-right:30%'> Hi Welcome <span style='color:blue'>{}</span> and Your age is <span style='color:red'>{}</span></h3>".format(name,a))

def employeedetails(request,sal,empid,empname):
	g = {"n":empname,"i":empid,"s":sal}
	return render(request,'prjc/sample.html',g)

def reg(request):
	if request.method == "POST":
		name = request.POST['n']
		age = request.POST['a']
		usname = request.POST['uname']
		pasd = request.POST['pwd']
		print(name,age,usname,pasd)
		return render(request,'prjc/display.html',{"na":name,"ag":age,"username":usname,"psd":pasd})
	return render(request,'prjc/register.html')

def lg(request):
	if request.method == "POST":
		u = request.POST['uname']
		p = request.POST['pwd']
		if u == "raju":
			if p == "123":
				return HttpResponse("Hi Welcome {}".format(u))
			return HttpResponse("Invalid password")
		return HttpResponse("Invalid Username")
	return render(request,'prjc/login.html')