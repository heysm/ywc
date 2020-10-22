from django.db import models
from datetime import datetime
# Create your models here.


class Gallery(models.Model):
    name = models.CharField(max_length=200, default="YWC")
    caption = models.TextField(max_length=500, default="you were chosen")
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=200, default='ywc art')
    artist = models.CharField(max_length=400, default="annonymous")
    category = models.CharField(max_length=200, blank=True)
    video_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    date = models.DateField(default=datetime.now)
    caption = models.TextField(default='''You Were Chosen is a new line of thought.

                               A line of thought to make people believe in their dreams, make people take authority of themselves and make a diverse and creative future.

                               Most importantly, to build a society that can learn to love each other, a society to feel that their lives have meaning, a society to feel that they are important.''')
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
