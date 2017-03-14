from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(blank=False, max_length=128, unique=False)
	profile_picture = models.ImageField(upload_to='static/images/profile_pictures', default="static/images/default.jpg")
	my_recipes = models.CharField(default=0, blank=True, max_length=128)
	saved_recipes = models.CharField(default=0, blank=True, max_length=128)

	def __str__(self):
		return self.user.username

class Recipe(models.Model):
	title = models.CharField(default="Recipe", blank=False, max_length=128)
	ingredients = models.CharField(default="ingredients", blank=False, max_length=128)
	instructions = models.CharField(default="instructions", blank=False, max_length=128)
	picture = models.ImageField(upload_to='static/images/recipe', blank=True)
	rating = models.IntegerField(default=0, blank=True)
	slug = models.SlugField(blank = True, unique = True)
	
	def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
		#change title to title+ID?
        super(Recipe, self).save(*args, **kwargs)

	def __str__(self):
		return self.title