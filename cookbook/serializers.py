import json

from .models import Ingredient

def serialize_ingredients(recipe):
    """
    Creates a dictionary of ingredient data for json.
    """
    try:
        ingredient_objects = Ingredient.objects.filter(recipe=recipe.id)
    except:
        return None
    else:
        ingredients = []
        for ingredient_object in ingredient_objects:
            # handle optional ingredient values
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
