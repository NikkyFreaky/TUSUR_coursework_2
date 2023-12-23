from django.shortcuts import render, redirect
from .components.parser import parse_news

# Create your views here.

def scrape(request):
    parse_news()
    return redirect("../")


def default(request):
    return render(request, 'default.html')