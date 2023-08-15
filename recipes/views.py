from django.http import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import *


class TagCreateView(CreateView):
    form_class = TagForm
    template_name = 'recipes/tag_form.html'
    
    def get_success_url(self):
        return reverse_lazy('recipes:tag-list')
    
class TagListView(ListView):
    model = Tag
    template_name = 'recipes/tags.html'
    context_object_name = 'tags'


class IngredientCreateView(CreateView):
    form_class = IngredientForm
    template_name = 'recipes/ingredient_form.html'
    
    def get_success_url(self):
        return reverse_lazy('recipes:ingredient-list')
    
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'recipes/ingredients.html'
    context_object_name = 'ingredients'
    

class RecipeCreateView(CreateView):
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    
    def get_success_url(self):
        return reverse_lazy('recipes:recipe-list')
    
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipe'
