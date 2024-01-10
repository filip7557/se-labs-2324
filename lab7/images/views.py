from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from django.urls import reverse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'images/home.html', context)

def image_list(request):
    sort=request.GET.get('sort', 'asc')
    if sort=="desc":
        images=Image.objects.order_by("-pub_date")
    else:
        images=Image.objects.order_by("pub_date")

    context = {
        'images': images,
    }
    return render(request, 'images/list.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    #comments= Comment.object,filter(image=image)
    comments= image.comment_set.all()
    context = {
        'image': image,
                'comments' : comments,

    }
    return render(request, 'images/detail.html', context)

def new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method=="POST":
        title=request.POST['title']
        url=request.POST['URL']
        pub_date=request.POST['pub_date']
        
        image= Image(user=request.user,title=title,url=url,pub_date=pub_date,)
        image.save()
        return HttpResponseRedirect(
            reverse('images:detail', args=(image.id,))
        )
    context= {}
    return render(request, 'images/new.html', context)

def new_comment(request, image_id):
    image= get_object_or_404(Image, pk=image_id)
    if request.method == "POST" and request.user.is_authenticated:
        text=request.POST['text']
        image.comment_set.create(
            text=text,
            user=request.user,
        )
    return HttpResponseRedirect(
        reverse('images:detail', args=(image_id,))
    )