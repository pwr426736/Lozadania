from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tytuł = models.CharField(max_length=200)
    treść = models.TextField()
    #image = models.ImageField(upload_to='post_images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tytuł + "\n" + self.treść

