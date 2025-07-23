from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required(login_url='/vege/login/')
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


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        print(username,password)
        users = User.objects.filter(username = username).values()
        print(users)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/vege/recipe/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/vege/login_page/')
    return render(request, 'login_page.html')

from django.contrib import messages
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(first_name, last_name, username, password)

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('/vege/register/')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, "Account created successfully")
        return redirect('/vege/register/')
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/vege/login_page/')