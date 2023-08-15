from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Film, Comments

admin.site.register(Film)
admin.site.register(Comments)
