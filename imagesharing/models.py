from django.db import models

# Create your models here.
class sharedimage(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='images')