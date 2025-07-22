from django.urls import path
from . import views
app_name = "vege"

#Url_config
urlpatterns = [
    path('recipe/', views.recipe, name="recipe"),
]