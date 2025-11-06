from django.urls import path
from .views import hello_notes_app


urlpatterns = [
    path('hello/', hello_notes_app),
]