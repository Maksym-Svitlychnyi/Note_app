from django.urls import path
from .views import hello_notes_app, notes_list


urlpatterns = [
    path('hello/', hello_notes_app, name='hello'),
    path('notes/', notes_list, name="notes"),
]