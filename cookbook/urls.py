from django.urls import path

from . import views

urlpatterns = [
    path('', views.TableOfContentsView, name='table_of_contents'),
    path('recipe/<recipe_title>', views.RecipeView, name='recipe'),
]
