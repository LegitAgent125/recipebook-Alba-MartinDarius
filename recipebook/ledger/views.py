from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'recipe_list.html', ctx)

def recipe(request):
    recipe = RecipeIngredient.objects.all()
    ctx = {
        "ingredient" : recipe
    }
    return render(request, 'recipe_detail.html', ctx)