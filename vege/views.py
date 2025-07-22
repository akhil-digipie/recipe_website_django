from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
        return redirect('/vege/recipe/')

    # Get all recipes to show them on the page
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))



    context = {'recipes': recipes}
    return render(request, 'recipe.html', context)
    # return redirect(request,'vege/recipe/',context)

# from django.http import HttpResponse
def delete_recipe(request, id):
    rec = Recipe.objects.get(id = id)
    rec.delete()
    print("Record Delete..")
    return redirect('/vege/recipe/')


def update_recipe(request, id):
    rec = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        rec.recipe_name = recipe_name
        rec.recipe_description = recipe_description

        if recipe_image:
           rec.recipe_image =  recipe_image
        rec.save()
        return redirect('/vege/recipe/')

    context = {'recipes': rec}
    return render(request, 'update_recipe.html', context)


def login(request):
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()

        return redirect('/register')
    return render(request,'register.html')
