from fractions import Fraction
from .models import Ingredient

def parse_ingredients(recipe):
    """
    Parses the ingredients and measurements for a given Recipe object.
    Returns a list of strings.
    """
    try:
        ingredients = Ingredient.objects.filter(recipe=recipe.id)
    except:
        return None
    else:
        parsed_ingredients = []
        for ingredient in ingredients:
            # handle optional ingredient values
            if ingredient.measurement:
                measurement = Fraction(ingredient.measurement)
            else:
                measurement = ""
            if ingredient.unit:
                unit = ingredient.unit
            else:
                unit = ""
            if ingredient.optional:
                optional = "(optional)"
            else:
                optional = ""

            # parse the ingredient string and append to list
            parsed_ingredient = "{} {} {} {}".format(measurement, unit, ingredient.name, optional)
            parsed_ingredients.append(parsed_ingredient)

        return parsed_ingredients
