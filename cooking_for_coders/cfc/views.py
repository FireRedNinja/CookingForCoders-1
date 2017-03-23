from django.conf.urls import url
from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from cfc.models import Recipe, UserProfile, Category
from cfc.forms import UserForm, UserProfileForm, RecipeForm


def index(request):

    context_dict = {}

    try:
        # request.session.set_test_cookie()
        top_recipes = Recipe.objects.order_by('-rating')[:4]
        newest_recipes = Recipe.objects.order_by('-created')[:4]
        veg_recipes = Recipe.objects.filter(category__id=2)[:4]
        lunch_recipes = Recipe.objects.filter(category__id=1)[:4]
        dessert_recipes = Recipe.objects.filter(category__id=3)[:4]
        category_list = Category.objects.order_by('title')
        # # top 4 rated (can't do rn)
        # visitor_cookie_handler(request)
        context_dict['top_recipes'] =  top_recipes
        context_dict['newest_recipes'] = newest_recipes
        context_dict['veg_recipes'] = veg_recipes
        context_dict['lunch_recipes'] = lunch_recipes
        context_dict['dessert_recipes'] = dessert_recipes
        context_dict['category_list'] = category_list

    except Recipe.DoesNotExist:
        context_dict[top_recipes] = None
        context_dict[newest_recipes] = None
        context_dict['category_list'] = None

    return render(request, 'cookingMain/index.html', context_dict)


def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(recipeID=recipe_id)
    except Recipe.DoesNotExist:
        recipe = None
    return render(request, 'cookingMain/recipe.html', {'recipe':recipe})


def show_category(request, category_title_slug):
    context_dict = {}
    try:
        category_list = Category.objects.order_by('title')
        category = Category.objects.get(slug=category_title_slug)
        recipes = Recipe.objects.filter(category=category)
        context_dict['recipes'] = recipes
        context_dict['category'] = category
        context_dict['category_list'] = category_list
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None
        context_dict['category_list'] = None
    return render(request, 'cookingMain/category.html', context_dict)


def add_recipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'cookingMain/add_recipe.html', {'form': form})


def splash(request):
    return render(request, 'cookingMain/splash.html', {})


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'registration/profile_registration.html', context_dict)


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return url('register_profile')


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'cookingMain/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})


def trendingRecipies(request):
    top_recipes = Recipe.objects.order_by('-rating')[:10]
    # trending recipes (can't do rn)
    return render(request, 'cookingMain/trendingRecipes.html', {})


def savedRecipies(request):
    return render(request, 'cookingMain/savedRecipes.html', {})

