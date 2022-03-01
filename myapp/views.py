from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from myapp.models import TechFest

# Create your views here.

class LandingPageView(View):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        techFest = TechFest.objects.all()
        return render(request, template_name="index.html", context={'techFest': techFest})