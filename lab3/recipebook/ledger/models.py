from datetime import datetime
from django.db import models
from django.urls import reverse


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.name

    def get_absolute_url(self):
           return reverse('ledger:recipe-detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='ingredients')

    class Meta:
        unique_together = [['ingredient', 'recipe'],]
        verbose_name = 'Recipe Ingredient'
        verbose_name_plural = 'Recipe Ingredients'
