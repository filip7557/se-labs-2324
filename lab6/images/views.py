from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def new(request):
    if request.method == "POST":
        title = request.POST['title']
        url = request.POST['url']
        pub_date = request.POST['pub_date']

        image = Image(title=title, url=url, pub_date=pub_date)
        image.save()
        return HttpResponseRedirect(reverse('images:detail', args=(image.id,)))
    context = {}
    return render(request, 'images/new.html', context)
    