from django.test import TestCase
from cfc.forms import *
from cfc.models import *
from cfc.urls import *
from cfc.views import *

# Create your tests here.

## Helper method
def add_user(username, email, password):
	user = UserProfile.objects.get_or_create(username=username)[0]
	user.emal = email
	user.password = password
	user.save()
	return user

def add_recipe(title, picture, description, ingredients, instructions):
	r = Recipe.objects.get_or_create(title=title)[0]
	r.picture = picture
	r.description = description
	r.ingredients = ingredients
	r.instruction = instructions
	r.save()
	return r

class RegisterTest(TestCase):
	
## does login adn register only appear when not logged in
## does createrecipe adn profile only apear when logged in
##

