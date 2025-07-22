from django.urls import path
from . import views
app_name = "vege"

#Url_config
urlpatterns = [
    path('recipe/', views.recipe, name="recipe"),
    path('delete_recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]