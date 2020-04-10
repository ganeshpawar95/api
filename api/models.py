from django.db import models

# Create your models here.
class Removebg(models.Model):
  images = models.ImageField(upload_to='')
   