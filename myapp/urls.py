from django.contrib import admin
from django.urls import path
from myapp.views import *
from myapp  import views

urlpatterns = [
    path("",LandingPageView.as_view(), name="home"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path("student-council/", StudentCouncilView.as_view(), name="student-council"),
    path("contact/", ContactView.as_view(), name="contact")

    
]
