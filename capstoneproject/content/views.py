from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def landing_page_view(request):
    context = {
        "name": "Home",
    }

    return render(request, "content/home.html", context)

def about_view(request):
    context = {
        "name": "About",
    }

    return render(request, "content/about.html", context)