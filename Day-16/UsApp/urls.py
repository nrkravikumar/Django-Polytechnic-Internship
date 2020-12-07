from django.urls import path
from UsApp import views

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.abts,name="ab"),
    path('cnt/',views.cntc,name="cn"),
    path('reg/',views.regis,name="rg"),
]
