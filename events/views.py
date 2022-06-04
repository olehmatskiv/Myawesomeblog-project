from django.shortcuts import render
from .models import Event
# Create your views here.

def home(request):
    events = Event.objects
    return render(request, 'events/index.html' , {'events' : events})