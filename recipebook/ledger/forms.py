from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        exclude = ['recipe'] # from https://testdriven.io/tips/ca45db78-da38-4ba0-884d-9be0bc1e3fbf/