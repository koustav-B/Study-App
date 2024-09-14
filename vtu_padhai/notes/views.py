from django.shortcuts import render
from .models import Note

# Welcome view with a list of uploaded notes
def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})
