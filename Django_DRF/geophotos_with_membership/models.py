from django.contrib.auth.models import User
from django.db import models

class GeoPhoto(models.Model):
    image = models.ImageField(upload_to='photos/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    comment = models.TextField(blank=True, null=True)  # New field for photo comment
    owner = models.ForeignKey(User, related_name='geophotos_with_membership', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "geophotos_with_membership"

    def __str__(self):
        return self.title

