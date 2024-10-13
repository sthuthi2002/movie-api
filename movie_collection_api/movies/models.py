from django.db import models
from django.contrib.auth.models import User
import uuid

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=255)
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Ensure this line exists

    def __str__(self):
        return self.title

# Movie model
class Movie(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)

    def __str__(self):
        return self.title