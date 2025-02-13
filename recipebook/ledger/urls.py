from django.urls import path
from .views import recipe_list, recipe_1, recipe_2

urlpatterns = [
path('recipes/list', recipe_list, name="recipes/list"),
path('recipe/1', recipe_1, name="recipe/1"),
path('recipe/2', recipe_2, name="recipe/2"),
]
# This might be needed, depending on your Django version
app_name = "ledger"
