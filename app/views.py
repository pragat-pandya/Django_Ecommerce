from django.http import request
from django.shortcuts import render

# Create your views here.

# Landing page of the website.
def index (request):
    # Further cookie based behaviour to be coded here.
    return render(request, "app/index.html")

# Fanbook View
def fanbook (request):
    return render (request, "app/fanbook.html")
