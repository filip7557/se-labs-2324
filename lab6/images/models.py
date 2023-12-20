from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=512)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}: {self.title}"
    
class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)