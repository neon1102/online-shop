from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'categories/')

    def __str__(self) -> str:
        return self.name


