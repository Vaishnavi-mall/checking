from django.contrib import admin
from django.urls import path
from myapp.views import LandingPageView
from myapp  import views

urlpatterns = [
    path("",LandingPageView.as_view(), name="home")
    
]
