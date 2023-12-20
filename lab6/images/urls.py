from django.urls import path
from .views import image_list, detail

app_name = "images"
urlpatterns = [
    path('', image_list, name="list"),
    # /images/5/ -> images:detail
    path('<int:image_id>/', detail, name="detail"),
]