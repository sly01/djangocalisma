from django.db import models

# Create your models here.

class Post(models.Model):
    yazar = models.CharField(max_length=20)
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
