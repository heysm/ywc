from django.shortcuts import render, get_object_or_404
from .models import Gallery
# Create your views here.


def home(request):
    gallery = Gallery.objects.all()
    return render(request, 'home/home.html', {"gallery": gallery})
