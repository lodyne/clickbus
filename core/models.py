from django.db import models
from PIL import Image
from django.urls import reverse

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=False, unique=True)
    image = models.ImageField(upload_to="images",height_field=None, width_field=None, max_length = None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    