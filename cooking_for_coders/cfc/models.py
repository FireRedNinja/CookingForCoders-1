from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.forms import ModelChoiceField

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	accountID = models.IntegerField(unique=True, blank=)
	name = models.CharField(blank=False, max_length=128, unique=False)
	profile_picture = models.ImageField(upload_to='static/images/profile_pictures', default="static/images/default.jpg")
	my_recipes = models.CharField(default=0, blank=True, max_length=128)
	saved_recipes = models.CharField(default=0, blank=True, max_length=128)

	def __str__(self):
		return self.user.username

class Recipe(models.Model):
	title = models.CharField(default="Recipe", blank=False, max_length=128)
	ingredients = models.TextField(default="Put your ingredients here!", blank=False)
	instructions = models.TextField(default="Type your instructions here!", blank=False)
	picture = models.ImageField(upload_to='static/images/recipe', blank=True)
	rating = models.IntegerField(default=0, blank=True)
	slug = models.SlugField(blank = True, unique = True)
	category = models.ModelChoiceField(queryset=Category.objects.all(), required=True)
	
	# def save(self, *args, **kwargs):
     #    self.slug = slugify(self.title)
	# 	#change title to title+ID?
     #    super(Recipe, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(blank=False, max_length=128)

	def __str__(self):
		return self.title

class SavedRecipe(models.Model):
    
