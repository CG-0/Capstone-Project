from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Seed

# Create your views here.
def landing_page_view(request):
    seed = Seed.objects.all().order_by('name').values

    context = {
        'seeds': seed,
    }

    return render(request, "content/home.html", context)

def about_view(request):
    context = {
        "name": "About",
    }

    return render(request, "content/about.html", context)

def detail_view(request, slug):
    slug = get_object_or_404(Seed, slug=slug)
    context = {
        'record': record,
    }

    return render(request, "content/detail.html", context)