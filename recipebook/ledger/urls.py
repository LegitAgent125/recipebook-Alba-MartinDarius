from django.urls import path
from .views import RecipeListView, RecipeDetailView, add_recipe, upload_recipe_img

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name="recipes/list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe/detail"),
    path('recipe/add', add_recipe, name='recipe/add'),
    path('recipes/<int:pk>/uploadimage', upload_recipe_img, name='upload_recipe_img'),
]

app_name = "ledger"
