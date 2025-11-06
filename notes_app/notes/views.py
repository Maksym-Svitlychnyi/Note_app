from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_notes_app(request):
    return HttpResponse("Hello from Notes app")