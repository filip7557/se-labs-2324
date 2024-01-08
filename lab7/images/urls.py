from django.urls import path
from .views import image_list, detail, new, new_comment

app_name = "images"
urlpatterns = [
    path('', image_list, name="list"),
    # /images/5/ -> images:detail
    path('<int:image_id>/', detail, name="detail"),
    # /images/new/ -> images:new
    path('new/', new, name="new"),
     # /images/new/ -> images:new
    path('<int:image_id>/comments/new/', new_comment, name="new_comment"),

]