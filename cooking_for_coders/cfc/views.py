from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView

def index(request):
    return render(request, 'cookingMain/index.html', {})

def recipe(request):
    return render(request, 'cookingMain/recipe.html', {})

def profile(request):
    return render(request, 'cookingMain/profile.html', {})

def splash(request):
    return render(request, 'cookingMain/splash.html', {})

def trendingRecipies(request):
    return render(request, 'cookingMain/trendingRecipes.html', {})

def savedRecipies(request):
	return render(request, 'cookingMain/savedRecipes.html', {})

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/cfc/'