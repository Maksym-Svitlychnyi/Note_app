from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_notes_app(request):
    return HttpResponse("Hello from Notes app")

def notes_list(request):
    notes = [
        {"title": "Купити продукти", "content": "Молоко, хліб, яйця"},
        {"title": "Вивчити Python", "content": "Здати усі домашні, Зробити фінальний проект"},
    ]
    return render(request, "notes.html", {"notes": notes})

