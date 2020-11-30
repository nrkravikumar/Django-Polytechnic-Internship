"""djinpoly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djpi import views
from djboot import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hel/',views.he),
    path('hll/<str:n>/',views.hlp),
    path('tbl/<int:t>/',views.tble),
    path('rcd/<str:name>/<int:age>/',views.record),
    path('std/<str:name>/<int:age>/<int:prc>/',views.stdnt),
    path('hle/<int:a>/<str:name>/',views.rcde),
    path('employee/<int:empid>/<str:empname>/<int:sal>/',views.employeedetails),
    path('register/',views.reg),
    path('login/',views.lg),
    path('home/',v.home),
    path('',v.strg,name="studentrg"),
]
