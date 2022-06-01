from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) 
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    
    def __str__(self):
        return self.description
