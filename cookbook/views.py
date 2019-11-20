from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

from .models import Recipe, Ingredient
from .parser import parse_ingredients

def RecipeView(request, recipe_title):
    try:
        recipe = Recipe.objects.get(title=recipe_title)
    except:
        recipe = None
    context = {
        'recipe': recipe,
        'ingredients': parse_ingredients(recipe)
    }
    return render(request, 'recipe.html', context)

def TableOfContentsView(request):
    recipe_list = Recipe.objects.order_by('title')
    context = {
        'recipe_list': recipe_list
    }
    return render(request, 'index.html', context)

def AddRecipeView(request):
    return render(request, 'add_recipe.html')