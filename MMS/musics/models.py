from django.db import models

class Music(models.Model):
    music_id = models.CharField(max_length=255)
    music_name = models.CharField(max_length=255)
    music_artist = models.CharField(max_length=255)
    music_genre = models.CharField(max_length=255)
    music_link = models.URLField(max_length=255, blank=True, null=True)  # New field for the link

# Create your models here.