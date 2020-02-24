import json

from .models import Ingredient

def serialize_ingredients(ingredient_objects):
    """
    Creates a dictionary of ingredient data for json.
    """
    ingredients = []
    for ingredient_object in ingredient_objects:
        if ingredient_object.quantity:
            quantity = ingredient_object.quantity
        else:
            quantity = ""
        if ingredient_object.unit:
            unit = ingredient_object.unit.lower()
        else:
            unit = ""
        if ingredient_object.optional:
            name = "{} {}".format(ingredient_object.name.lower(), "(optional)")
        else:
            name = ingredient_object.name

        ingredient = {
            'quantity': quantity,
            'unit': unit,
            'name': name
        }
        ingredients.append(ingredient)
    return ingredients
