from django.shortcuts import render

from .models import Recipe, Ingredient
from .serializers import serialize_ingredients

def RecipeView(request, recipe_title):
    try:
        recipe = Recipe.objects.get(title=recipe_title)
    except:
        recipe = None
    context = {
        'recipe': recipe,
        'ingredients': Ingredient.objects.filter(recipe=recipe.id),
        'serialized_ingredients': serialize_ingredients(recipe)
    }
    return render(request, 'recipe.html', context)

def TableOfContentsView(request):
    context = {
        'recipe_list': Recipe.objects.order_by('title')
    }
    return render(request, 'index.html', context)

def AddRecipeView(request):
    return render(request, 'add_recipe.html')
