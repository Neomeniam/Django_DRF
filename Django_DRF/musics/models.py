from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='musics', on_delete=models.CASCADE)

    class Meta:
        db_table = "music"
    def __str__(self):
        return f"Photo by {self.owner.username} at ({self.latitude}, {self.longitude})"

