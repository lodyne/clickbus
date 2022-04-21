from django.db import models
from PIL import Image

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media",height_field=None, width_field=None, max_length = None)
    created_at = models.DateField(auto_now=False,auto_now_add=False)
    updated_at = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name
    