from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdimin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

    
