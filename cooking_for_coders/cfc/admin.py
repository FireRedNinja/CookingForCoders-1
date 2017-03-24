from django.contrib import admin
from cfc.models import Recipe, Category, UserProfile, StoredRecipe


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(UserProfile)
admin.site.register(StoredRecipe)


# Register your models here.
