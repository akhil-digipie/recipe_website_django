from django.contrib import admin

from .models import *
from .views import recipe

admin.site.register(Recipe)