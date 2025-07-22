from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField()
    recipe_description = models.TextField()
    recipe_image = models.ImageField()
