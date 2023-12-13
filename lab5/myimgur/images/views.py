from django.shortcuts import render, get_object_or_404
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

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    context = {
        'image': image,
    }
    return render(request, 'images/detail.html', context)