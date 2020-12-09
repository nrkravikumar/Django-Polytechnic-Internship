from django.urls import path
from UsApp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.abts,name="ab"),
    path('cnt/',views.cntc,name="cn"),
    path('reg/',views.regis,name="rg"),
    path('lg/',v.LoginView.as_view(template_name="sa/login.html"),name="log"),
    path('ds/',views.dashboard,name="dsh"),
    path('lgo/',v.LogoutView.as_view(template_name="sa/logout.html"),name="lgg"),
    path('ml/',views.mailsnd,name="ms"),
]
