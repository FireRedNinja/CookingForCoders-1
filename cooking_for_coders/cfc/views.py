from django.conf.urls import url
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from cfc.models import Recipe, UserProfile, Category, StoredRecipe
from cfc.forms import UserForm, UserProfileForm, RecipeForm


def index(request):

    context_dict = {}

    try:
        # request.session.set_test_cookie()
        top_recipes = Recipe.objects.order_by('-averageRating')[:4]
        newest_recipes = Recipe.objects.order_by('-created')[:4]
        veg_recipes = Recipe.objects.filter(category__id=2)[:4]
        snack_recipes = Recipe.objects.filter(category__id=1)[:4]
        dessert_recipes = Recipe.objects.filter(category__id=3)[:4]
        main_recipes = Recipe.objects.filter(category__id=4)[:4]
        category_list = Category.objects.order_by('title')
        # # top 4 rated (can't do rn)
        # visitor_cookie_handler(request)
        context_dict['top_recipes'] =  top_recipes
        context_dict['newest_recipes'] = newest_recipes
        context_dict['veg_recipes'] = veg_recipes
        context_dict['snack_recipes'] = snack_recipes
        context_dict['main_recipes'] = main_recipes
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
    return render(request, 'cookingMain/recipe.html', {'recipe':recipe, 'recipeID':recipe_id})


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

@login_required
def add_recipe(request):
	# try:
	# 	category = Category.objects.get(slug=category_title_slug)
	# except Category.DoesNotExist:
	# 	category = None

	form = RecipeForm()

	if request.method == 'POST':
		form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            Recipe = form.save(commit=False)
            Recipe.author = request.user.username
            Recipe.save()
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
    context_dict = {}
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/accounts/register/')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})

    try:
        stored_list = StoredRecipe.objects.filter(user=user)
        stored_recipes = Recipe.objects.filter()
    except Recipe.DoesNotExist:
        context_dict['recipes_saved'] = None

    try:
        my_recipes = Recipe.objects.filter(author=username)
    except Recipe.DoesNotExist:
        context_dict['my_recipes'] = None


    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    context_dict = {'userprofile': userprofile, 'selecteduser': user, 'form': form, 'my_recipes':my_recipes, 'recipes_saved':stored_list}

    return render(request, 'cookingMain/profile.html', context_dict)


@login_required
def add_rating(request):
    if request.method == 'POST':
        rating = request.rate
        rating.save()
        print rating
    return HttpResponse("Rating Submitted")


@login_required
def recipeStore(request, recipe_id):
    """Take the recipe id and the user id passed via the url check that the recipe is not
       already stored for that user then store it if it is
    """
    stored = StoredRecipe.objects.filter(recipe=recipe_id, user=request.user.id)
    if stored:
        output = ("Recipe already in your favorites!")
        return HttpResponse(output)
    else:  # save the recipe
        r = get_object_or_404(Recipe, pk=recipe_id)
        new_store = StoredRecipe(recipe=r, user=request.user)
        new_store.save()
        output = ("Recipe added to your favorites!")
        return HttpResponse(output)


@login_required
def recipeUnStore(request):
    """Take the recipe id via the url check that the recipe is not already
       stored for that user then remove it if it is
    """
    if request.method == 'POST':
        if request.POST['recipeID']:
            try:
                stored_recipe = StoredRecipe.objects.get(recipe=request.POST['recipeID'], user=request.user.id)
            except StoredRecipe.DoesNotExist:
                raise Http404
            stored_recipe.delete()
            return redirect('/recipe/ajax-favrecipe/')



