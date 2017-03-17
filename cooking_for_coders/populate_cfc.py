import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cooking_for_coders.settings')

import django
django.setup()
from cfc.models import Category, Recipe, UserProfile

def populate():

    Vegetarian_rec = [
        {"title": "Spicy Courgette Python Pockets"}
    ]
