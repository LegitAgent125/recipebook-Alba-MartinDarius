from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm

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
    images = RecipeImage.objects.all()
    ctx = {
        "ingredient" : recipe,
        "image" : images
    }
    return render(request, 'recipe_detail.html', ctx)

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('/recipes/list')
    else:
        form = RecipeForm()

    return render(request, 'recipe_add.html', {'form': form})

def upload_recipe_img(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeImageForm()
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False) 
            image.recipe = recipe 
            image.save()
            return redirect("ledger:recipe/detail", recipe.pk)

    return render(request, 'recipe_image.html', {'form': form, 'recipe': recipe})