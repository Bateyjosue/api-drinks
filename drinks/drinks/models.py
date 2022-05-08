from django.db import models

# Create your models here.

class Category(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Drinks(models.Model):
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
