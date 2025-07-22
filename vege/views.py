from django.shortcuts import render
from .models import Recipe

def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # Save to database
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

    # Get all recipes to show them on the page
    recipes = Recipe.objects.all()

    return render(request, 'recipe.html', {'recipes': recipes})
