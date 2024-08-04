from django.db import models

# Create your models here.

class Tourist(models.Model):
    spotname = models.CharField(max_length = 250)
    place = models.CharField(max_length = 250)
    city = models.CharField(max_length = 250)
    state = models.CharField(max_length = 250)
    country = models.CharField(max_length = 250)
    spotimage = models.ImageField(upload_to='images/')
    googlemap = models.URLField()

    def __str__(self):
        return '{}' . format(self.spotname)