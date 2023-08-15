from django.urls import path
from .views import *

app_name = 'recipes'

urlpatterns = [
    path('tag-create/', TagCreateView.as_view(), name='tag-form'),
    path('tags/', TagListView.as_view(), name='tag-list'),

    path('ingredient-create/', IngredientCreateView.as_view(), name='ingredient-form'),
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),

    path('recipe-create/', RecipeCreateView.as_view(), name='recipe-form'),
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    # path('', index),
]