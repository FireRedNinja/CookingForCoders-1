from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Category(models.Model):
	title = models.CharField(blank=False, max_length=128, unique=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title


class Recipe(models.Model):
    title = models.CharField(default="Recipe", blank=False, max_length=128)
    recipeID = models.AutoField(primary_key=True)
    ingredients = models.TextField(default="Put your ingredients here!", blank=False)
    instructions = models.TextField(default="Type your instructions here!", blank=False)
    description = models.CharField(default="Put a short description here!", max_length=64, blank=False)
    picture = models.ImageField(upload_to='recipe/', blank=False)
    rating = models.IntegerField(default=0, blank=True)
    # rating_count = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=False)
    category = models.ForeignKey(Category)
    author = models.CharField(max_length=128, unique=False, blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipeID)
        #change title to title+ID?
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class StoredRecipe(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.recipe.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    accountID = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class RateRecipe(models.Model):
	recipe = models.ForeignKey(Recipe)
	user = models.OneToOneField(User)
	rating = models.IntegerField(blank=True)

	def __str__(self):
		return self.rating
