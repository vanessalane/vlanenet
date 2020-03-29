from django.core.validators import MinValueValidator
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
        (CUP, 'c'),
        (DECILITER, 'dl'),
        (GRAM, 'g'),
        (GALLON, 'gal'),
        (FLUID_OUNCE, 'fl oz'),
        (LITER, 'l'),
        (POUND, 'lb'),
        (MILLIGRAM, 'mg'),
        (MILLILITER, 'ml'),
        (OUNCE, 'oz'),
        (PINCH, 'pinch'),
        (PINT, 'pt'),
        (QUART, 'qt'),
        (TABLESPOON, 'tbsp'),
        (TEASPOON, 'tsp')
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField(validators=[MinValueValidator(0,message="Can't have a negative quantity")], null=True, blank=True)
    unit = models.CharField(
        max_length=10,
        choices=UNIT_OPTIONS,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    optional = models.BooleanField(default=False)

    def __str__(self):
        return self.name
