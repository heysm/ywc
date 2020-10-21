from django.db import models

# Create your models here.


class Gallery(models.Model):
    name = models.CharField(max_length=200, default="YWC")
    caption = models.TextField(max_length=500, default="you were chosen")
    image_url = models.URLField(blank=True)
