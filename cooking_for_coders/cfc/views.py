from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from cfc.models import Recipe, UserProfile
#from cfc.forms import


def index(request):

    context_dict = {}

    try:
        # request.session.set_test_cookie()
        # newest_recipes = Recipe.objects.filter(pub_date__lte=datetime.now()-10)order_by('-pub_date')[:4]
        top_recipes = Recipe.objects.order_by('-rating')[:4]
        # # top 4 rated (can't do rn)
        # visitor_cookie_handler(request)
        context_dict = {'top_recipes': top_recipes}

    except Recipe.DoesNotExist:
        context_dict[top_recipes] = None

    return render(request, 'cookingMain/index.html', context_dict)

def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        recipe = None
    return render(request, 'cookingMain/recipe.html', {'recipe':recipe})

def profile(request):
    return render(request, 'cookingMain/profile.html', {})

def splash(request):
    return render(request, 'cookingMain/splash.html', {})

def trendingRecipies(request):
    top_recipes = Recipe.objects.order_by('-rating')[:10]
    # trending recipes (can't do rn)
    return render(request, 'cookingMain/trendingRecipes.html', {})

def savedRecipies(request):
    return render(request, 'cookingMain/savedRecipes.html', {})

