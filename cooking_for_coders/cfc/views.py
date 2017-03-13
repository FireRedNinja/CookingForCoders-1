from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'cookingMain/index.html', {})

def recipe(request):
    return render(request, 'cookingMain/recipe.html', {})

def profile(request):
    return render(request, 'cookingMain/profile.html', {})

def splash(request):
    return render(request, 'cookingMain/splash.html', {})

