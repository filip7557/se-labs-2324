from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=512)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}: {self.title}"
    
    def liked_by(self, user):
        if isinstance(user, User):
            return user.like_set.filter(image=self).count() > 0
        else:
            return False
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text=models.CharField(max_length=512)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}: {self.image.title} -> {self.text}"
    
    def name(self):
        return f"{self.user.username} ({self.user.email})"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
