from django.urls import path
from . import views
app_name = "vege"

#Url_config
urlpatterns = [
    path('recipe/', views.recipe, name="recipe"),
    path('delete_recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout_page/', views.logout_page, name='logout_page'),

]