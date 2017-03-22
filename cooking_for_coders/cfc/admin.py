from django.contrib import admin
from cfc.models import Recipe, Category, UserProfile


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(UserProfile)


# Register your models here.
