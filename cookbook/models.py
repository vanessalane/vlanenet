from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    yield_count = models.PositiveSmallIntegerField()
    yield_units = models.CharField(max_length=50)
    prep_time = models.PositiveSmallIntegerField()
    cook_time = models.PositiveSmallIntegerField()
    MINUTES = 'MINS'
    HOURS = 'HRS'

    TIME_UNIT_OPTIONS = [
        (MINUTES, 'minutes'),
        (HOURS, 'hours')
    ]
    time_units = models.CharField(
        max_length=50,
        choices=TIME_UNIT_OPTIONS,
        default=MINUTES
    )
    instructions = models.TextField()
    source = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    optional = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField(null=True, blank=True)

    TEASPOON = 'TSP'
    TABLESPOON = 'TBSP'
    CUP = 'C'
    FLUID_OUNCE = 'FL_OZ'
    QUART = 'QT'
    PINT = 'PT'
    GALLON = 'GAL'
    MILLILITER = 'ML'
    LITER = 'L'
    DECILITER = 'DL'
    OUNCE = 'OZ'
    POUND = 'LB'
    MILLIGRAM = 'MG'
    GRAM = 'G'
    PINCH = 'PINCH'

    UNIT_OPTIONS = [
        (TEASPOON, 'tsp'),
        (TABLESPOON, 'tbsp'),
        (CUP, 'c'),
        (FLUID_OUNCE, 'fl oz'),
        (QUART, 'qt'),
        (PINT, 'pt'),
        (GALLON, 'gal'),
        (MILLILITER, 'ml'),
        (LITER, 'l'),
        (DECILITER, 'dl'),
        (OUNCE, 'oz'),
        (POUND, 'lb'),
        (MILLIGRAM, 'mg'),
        (GRAM, 'g'),
        (PINCH, 'pinch')
    ]
    unit = models.CharField(
        max_length=10,
        choices=UNIT_OPTIONS,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
