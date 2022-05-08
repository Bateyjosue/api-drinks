from django.db import models

# Create your models here.

class Drinks(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name