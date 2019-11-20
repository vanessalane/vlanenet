from django.urls import path

from . import views

urlpatterns = [
    path('', views.TableOfContentsView, name='table_of_contents'),
    path('<recipe_title>', views.RecipeView, name='recipe'),
    path('add_recipe', views.AddRecipeView, name='add_recipe'),
]
