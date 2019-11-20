from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    yield_count = models.PositiveSmallIntegerField()
    yield_units = models.CharField(max_length=50)
    prep_time = models.PositiveSmallIntegerField()
    cook_time = models.PositiveSmallIntegerField()
    time_units = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    measurement = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    optional = models.BooleanField(default=False)

    def __str__(self):  
        return self.name
