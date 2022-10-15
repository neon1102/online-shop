from cProfile import label
from django.db import models

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=50)
    email_adress = models.EmailField(max_length=40)
    company = models.CharField(max_length=50)
    telephone  = models.IntegerField()
    address = models.CharField(max_length=100)
    comments = models.TextField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.first_name