from django.urls import path
from . import views
app_name = "home"

#Url_config
urlpatterns = [
    path('index/', views.say_hello, name="index"),
    path('contact/', views.contact, name="contact")
]