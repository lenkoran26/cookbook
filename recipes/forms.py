from django import forms
from .models import Tag, Ingredient, Recipe, AmountIngredient


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    amount = forms.IntegerField(widget=forms.widgets.NumberInput(attrs={'min':0}))
    class Meta:
        model = Recipe
        fields = ['name']



