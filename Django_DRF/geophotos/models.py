from django.db import models

class GeoPhoto(models.Model):
    image = models.ImageField(upload_to='photos/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    