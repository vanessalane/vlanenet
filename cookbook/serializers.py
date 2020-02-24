import json

from .models import Ingredient

def serialize_ingredients(ingredient_objects):
    """
    Creates a dictionary of ingredient data for json.
    """
    ingredients = []
    for ingredient_object in ingredient_objects:
        if ingredient_object.optional:
            name = "{} {}".format(ingredient_object.name, "(optional)")
        else:
            name = ingredient_object.name
        ingredient = {
            'quantity': ingredient_object.quantity,
            'unit': ingredient_object.unit,
            'name': name
        }
        ingredients.append(ingredient)
    return ingredients
