from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from datetime import datetime
from cfc.models import Recipe, UserProfile
#from cfc.forms import



def index(request):
    request.session.set_test_cookie()
    newest_recipes = Recipe.objects.filter(pub_date__lte=datetime.now()-10)order_by('-pub_date')[:4]
    top_recipes = Recipe.objects.order_by('-rating')[:4]
    # top 4 rated (can't do rn)
    visitor_cookie_handler(request)

    return render(request, 'cookingMain/index.html', {})

def recipe(request):
    try:
        recipe = Recipe.objects.get(slug=recipe_id_slug)
    except Recipe.DoesNotExist:
        recipe = None
    return render(request, 'cookingMain/recipe.html', {})

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

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/cfc/'
