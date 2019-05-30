from django.db import models
from django.contrib import admin  #para usar el decorador

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    photo = models.ImageField(upload_to = 'cars' , null=True) #para soportar este necesitamos instalar el paquete Pillow
    videofile= models.FileField(upload_to='videos/', null=True)
    
    def __str__(self):
        return self.name