from django.shortcuts import render
from django.http import HttpResponse

from .models import Image

# Create your views here.
def home(request):
    context = {}
    return render(request, 'images/home.html', context)

def image_list(request):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'images/list.html', context)