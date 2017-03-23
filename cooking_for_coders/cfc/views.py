from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from cfc.models import Recipe, UserProfile, Category
from cfc.forms import UserForm, UserProfileForm


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


def profile(request):
    return render(request, 'cookingMain/profile.html', {})


def splash(request):
    return render(request, 'cookingMain/splash.html', {})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:

            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'registration/registration_form.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def trendingRecipies(request):
    top_recipes = Recipe.objects.order_by('-rating')[:10]
    # trending recipes (can't do rn)
    return render(request, 'cookingMain/trendingRecipes.html', {})


def savedRecipies(request):
    return render(request, 'cookingMain/savedRecipes.html', {})

