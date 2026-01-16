from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def landing_page_view(request):
    return HttpResponse("<h1>SeedBank</h1><p>Welcome to my project for WEB 3200!</p>")