from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    accountID = models.IntegerField(unique=True, blank=False)
    name = models.CharField(blank=False, max_length=128, unique=False)
    profile_picture = models.ImageField(upload_to='static/images/profile_pictures', default="static/images/default.jpg")
    my_recipes = models.CharField(default=0, blank=True, max_length=128)
    saved_recipes = models.CharField(default=0, blank=True, max_length=128)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(blank=False, max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(default="Recipe", blank=False, max_length=128)
    recipeID = models.IntegerField(unique=True, blank=False)
    ingredients = models.TextField(default="Put your ingredients here!", blank=False)
    instructions = models.TextField(default="Type your instructions here!", blank=False)
    description = models.CharField(default="Put a short description here!", max_length=64, blank=False)
    picture = models.ImageField(upload_to='media/recipe/', blank=True)
    rating = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category)
    #user_created = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipeID)
        #change title to title+ID?
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipeID


class SavedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(UserProfile)


    def __str__(self):
        return self.recipe




    
