from django.urls import path
from DailyWorkStatus import views

urlpatterns = [
	path("",views.home,name="hm"),
]