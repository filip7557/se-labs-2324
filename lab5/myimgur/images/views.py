from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'images/home.html', context)

def image_list(request):
    context = {}
    return render(request, 'images/list.html', context)