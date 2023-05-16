from django.db import models

# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=200)

    
    image = models.ImageField(blank=True, upload_to='shopping/')