from django.db import models


# Create your models here.

class contactdetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=170)
    message=models.TextField()

    def __str__(self):
        return self.name
