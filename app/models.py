from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(validators=[MinValueValidator(0)])
