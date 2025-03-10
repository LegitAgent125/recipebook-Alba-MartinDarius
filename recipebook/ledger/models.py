from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}: Ingredient'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ingredient', args=[self.pk])
    
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: Recipe'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe/detail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)
    
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
    )
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)