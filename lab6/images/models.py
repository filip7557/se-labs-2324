from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=512)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}: {self.title}"