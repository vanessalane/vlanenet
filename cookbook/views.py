from django.shortcuts import render

from .models import Recipe, Ingredient
from .serializers import serialize_ingredients

def RecipeView(request, recipe_title):
    try:
        recipe = Recipe.objects.get(title=recipe_title)
    except:
        recipe = None
    ingredients = Ingredient.objects.filter(recipe=recipe.id)
    for ingredient in ingredients:
        if ingredient.quantity and ingredient.quantity % 1 == 0:
            ingredient.quantity = int(ingredient.quantity)
    context = {
        'recipe': recipe,
        'serialized_ingredients': serialize_ingredients(ingredients),
        'ingredients': ingredients
    }
    return render(request, 'recipe.html', context)

def TableOfContentsView(request):
    context = {
        'recipe_list': Recipe.objects.order_by('title')
    }
    return render(request, 'index.html', context)

def AddRecipeView(request):
    return render(request, 'add_recipe.html')
