import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cooking_for_coders.settings')

import django

django.setup()
from cfc.models import Category, Recipe


def populate():
    vegetarian_rec = [
        {"title": "Spicy Courgette Python Pockets", "recipeid": "12345",
         "ingredients": "2 Courgettes, 1tbsp Chilli Powder, 1 Chilli, 200g Grated Cheddar",
         "instructions": "1. Slice courgettes in half \n 2. Finely slice Chilli \n 3. Put chilli on courgettes, add chilli powder \n 4. Cook in oven for 15mins at 200degreesC"
            , "picture": "pockets.jpg", "rating": "3", "category": "Vegetarian"}
    ]

    main_rec = [
        {"title": "Spicy Courgette Python Pockets", "recipeid": "123",
         "ingredients": "2 Courgettes, 1tbsp Chilli Powder, 1 Chilli, 200g Grated Cheddar",
         "instructions": "1. Slice courgettes in half \n 2. Finely slice Chilli \n 3. Put chilli on courgettes, add chilli powder \n 4. Cook in oven for 15mins at 200degreesC"
            , "picture": "pockets.jpg", "rating": "3", "category": "Main"}
    ]

    dessert_rec = [
        {"title": "Hot Chocolate Brownie", "recipeid": "21423",
         "ingredients": "2 Courgettes, 1tbsp Chilli Powder, 1 Chilli, 200g Grated Cheddar",
         "instructions": "1. Slice courgettes in half \n 2. Finely slice Chilli \n "
                         "3. Put chilli on courgettes, add chilli powder \n 4. Cook in oven for 15mins at 200degreesC"
            , "picture": "brownie.jpg", "rating": "5", "category": "Dessert"}
    ]

    cats = {"Vegetarian": {"recipe": vegetarian_rec},
             "Main": {"recipe": main_rec},
             "Dessert": {"recipe": dessert_rec}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for r in cat_data["recipe"]:
            add_rec(c, r["title"], r["recipeid"], r["ingredients"], r["instructions"], r["picture"], r["rating"], r["category"])

    for c in Category.objects.all():
        for r in Recipe.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(r)))


def add_rec(cat, title, recipeid, ingredients, instructions, picture, rating, category):
    r = Recipe.objects.get_or_create(category=cat, title=title) [0]
    r.title=title
    r.recipeid=recipeid
    r.ingredients=ingredients
    r.instructions=instructions
    r.picture=picture
    r.rating=rating
    r.category=category
    r.save()
    return r

def add_cat(title):
    c = Category.objects.get_or_create(title=title) [0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting CFC population script...")
    populate()
