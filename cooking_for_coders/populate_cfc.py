import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cooking_for_coders.settings')

import django

django.setup()
from cfc.models import Category, Recipe

from django.utils import timezone


def populate():
    vegetarian_rec = [
        {"title": "Spicy Courgette Python Pockets",
         "ingredients": "2 Courgettes, 1tbsp Chilli Powder, 1 Chilli, 200g Grated Cheddar",
         "instructions": "1. Slice courgettes in half \n 2. Finely slice Chilli \n 3. Put chilli on courgettes, add chilli powder \n 4. Cook in oven for 15mins at 200degreesC", "description":"Moist pockets of juicy, spicy courgette",
         "picture": "recipe/pockets.jpg", "rating": "3", "category": "Vegetarian", "author":"itsmaboi"},

        {"title": "SWEET & SOUR CUCUMBER NOODLES WITH SOBA",
         "ingredients": "4 ounces soba noodles, 1 Tablespoon soy sauce, 2-3 spiralised medium cucumbers, 0.5 cup rice vinegar, 2 teaspoons honey, for topping: green onions & sesame seeds",
         "instructions": "1. Cook the soba noodles in boiling water for 7-8 mins then drain and add soy sauce. \n 2. In a large bowl whisk rice vinegar and honey into dressing. \n 3. Coat cucumber in dressing and set asside for 30 mins \n 4. Mix cucumber and noodles. \n 5. Serve with sprinkled green onions and sesame seeds.",
         "description": "Delicious light noodle meal",
         "picture": "recipe/noodles.jpg", "rating": "5", "category": "Vegetarian", "author":"itsmaboi"}





    ]

    main_rec = [
        {"title": "Wonderful Short Ribs",
         "ingredients": "1 (28 ounce) can tomato sauce, 3 tablespoons lemon juice, 4 teaspoons Worcestershire sauce, 2 tablespoons dried parsley, 1 teaspoon dried thyme, 2 bay leaves, 2 tablespoons brown sugar, 2 teaspoons salt, 1 teaspoon crushed red pepper flakes, 1 medium onion cut into rings, 3 pounds beef short ribs",
         "instructions": "1. In a large pan over medium-high heat, stir in tomato sauce, lemon juice, and Worcestershire sauce. Stir in parsley, thyme, bay leaves, brown sugar, salt, and red pepper flakes. Add onions and short ribs, and stir together until the mixture comes to a boil. \n 2.Cover, reduce heat to medium low, and simmer; stirring occasionally and skimming fat from surface, until meat is tender, about 2 1/2 hours. Remove bay leaves before serving."
            ,"description":"This tender meat that falls right off the bone is great served over rice!", "picture": "recipe/ribs.jpg", "rating": "5",  "category": "Main", "author":"itsmaboi"} ,

        {"title": "Classic BLT Sandwhich",
         "ingredients": "3 slices bacon, 2 slices white bread, 2 leaves lettuce, 2 sliced tomatoes, 2 spoons mayo",
         "instructions": "1. Begin frying bacon. \n 2. Toast bread. \n 3. Spread mayo on toast. \n 4. Add lettuce and tomato. \n 5. Add bacon once crispy. \n 6. Add top bit of toast and enjoy."
            ,"description": "Amazing sandwhich without fault!","picture": "recipe/blt.jpg", "rating": "3", "category": "Main","author":"itsmaboi"} ,

        {"title": "Easy Pizza Muffin",
         "ingredients": "1 English muffin, 1 tablespoon pizza sauce or 1 tablespoons tomato paste, 1 cup cheese, + any other desired toppings",
         "instructions": "1. Cut the muffin in half. \n 2. Spread with sauce. \n 3. Add toppings. \n 4. Cook under grill or in oven until cheese melts."
            , "description": "Quick and easy, great for kids.", "picture": "recipe/pizzamuffin.jpg", "rating": "2", "category": "Main", "author":"itsmaboi"} ,

        {"title": "Mushroom Quesadilla",
         "ingredients": "2 lbs fresh sliced mushrooms, 1.5 tablespoons minced garlic, salt & pepper, 4 large tortillas, 1.25 cups grated cheddar cheese",
         "instructions": "1. Wrap the tortillas in foil and warm them in a 350F oven while you are cooking the mushrooms. \n 2. Saute the mushrooms and garlic until most of the water from the mushrooms has evaporated. \n 3. Season with salt & pepper. \n 4. Divide the mushrooms & cheese between the four tortillas, fold in half. \n 5. Serve with salsa, quacamole & sour cream (Optional)."
            , "description": "Makes a tasty lunch, mushrooms and cheese go together well.", "picture": "recipe/mushquesa.jpg", "rating": "4", "category": "Main", "author":"itsmaboi"}


    ]

    dessert_rec = [
        {"title": "Hot Chocolate Brownie",
         "ingredients": "1 (4 ounce) package instant chocolate pudding mix, any ingredients required by pudding mix, 1 (18 ounce) box chocolate cake mix, 2 cups semi-sweet chocolate chip, confectioners' sugar",
         "instructions": "1. Prepare pudding according to package directions. \n 2. Whisk in cake mix. \n "
                         "3. Stir in chocolate chips. \n 4. Pour into a greased 15- x 10- x 1-inch baking pan. \n 5. Bake at 350 degrees Farenheight for 30 to 35 minutes or until the top springs back when lightly touched. \n 6. Dust with confectioner's sugar."
            ,"description":"Hot wet brownie stuffed oozing chocolate", "picture": "recipe/brownie.jpg", "rating": "5",  "category": "Dessert","author":"itsmaboi"},

        {"title": "Apple Crisp",
         "ingredients": "3 cups sliced apples, 1 cup brown sugar, 0.5 cup flour, 0.25 cup butter, 0.33 cup chopped walnuts",
         "instructions": "1. Arrange apple slices in an 8-inch square baking dish. \n 2. Combine flour, sugar and butter, mixxing with hands until small lumps form. \n 3. Add nuts and sprinkle over apples. \n 4. Bake at 375 degrees farenheight for 40-45 minutes or until apples are tender and top is lightly browned. \n 5. Server warm with icecream(optional)",
         "description": "Sweet apple crisp to have with icecream.",
         "picture": "recipe/applecrisp.jpg", "rating": "3", "category": "Dessert", "author":"itsmaboi"} ,

        {"title": "Strawberry Pie",
         "ingredients": "1 pint washed and hulled strawberry, 1 cup sugar, 1 cup water, 3 tablespoons cornstarch, 1 prebaked pie shell",
         "instructions": "1. Mix water sugar and cornstarch in small saucepan. \n 2. Bring to boil stirring often. \n 3. When mixture thickens and turns transparent, remove from heat add strawberries and pour into baked pie shell. \n 4. Refrigerate to set top. \n 5. Serve with Cream(optional)",
         "description": "Delicious Strawberry Pie, hard to just have one piece!",
         "picture": "recipe/strawberrypie.jpg", "rating": "3", "category": "Dessert", "author":"itsmaboi"} ,

        {"title": "Easy Key Lime Pie",
         "ingredients": "14 ounces sweetened condensed milk, 0.5 cup key lime juice, 8 ounces whipped topping, 1 chocolate wafer pie crust",
         "instructions": "1. Beat milk and lime juice until smooth and thickened, fold in whipped topping. \n 2. Spoon into pie crust. \n 3. Cover and refrigerate for 1 hour to overnight.",
         "description": "Stunningly simple and superbly tasty!",
         "picture": "recipe/keylime.jpg", "rating": "5", "category": "Dessert", "author":"itsmaboi"}




    ]

    snack_rec = [
        {"title": "Butterscotch Oatmeal",
         "ingredients": "1 egg, beaten,1 3/4 cups milk, 1/2 cup packed brown sugar, 1 cup rolled oats, 2 tablespoons butter",
         "instructions":"1. In a saucepan over medium heat, whisk together the egg, milk and brown sugar. \n 2. Mix in the oats. \n 3. When the oatmeal begins to boil, cook and stir until thick. \n 4. Remove from the heat, and stir in butter until melted."
        ,   "description":"The best oatmeal ever. No need for extra sugar and great with out without milk", "picture": "recipe/butterscotchoatmeal.jpg", "rating":"5", "category": "Snack", "author":"itsmaboi"},

        {"title": "Peanut Butter Cookies",
         "ingredients": "1 cup peanut butter, 1 cup granulated sugar, 1 large egg",
         "instructions": "1. Mix peanut butter, sugar, and egg together until smooth. \n 2. Drop by teaspoon onto cookie sheet two inches apart. If desired, roll in extra sugar before placing on cookie sheet.. \n 3. Press with fork; press again in opposite direction. \n 4. Bake 10 to 12 minutes at 350 degrees Fahrenheit."
        ,   "description": "These are the quickest, simplest peanut butter cookies that you will ever make and they taste great!","picture": "recipe/pbuttercookies.jpg", "rating": "4", "category": "Snack", "author":"itsmaboi"},

        {"title": "Spinach Salad",
         "ingredients": "1 (6 ounce) package baby spinach leaves, 5 chopped hard-boiled eggs, 0.5 lb bacon, fried and crumbled, 1 thinly sliced medium red onion, 1 jar poppy seed dressing",
         "instructions": "1. Place freshly washed spinach on individual plates. \n 2. Sprinkle with chopped hard boiled eggs and crumbled bacon. \n 3. Spread sliced onion on top. \n 4. Drizzle with poppyseed dressing.",
         "description": "Great alternative salad recipe!",
         "picture": "recipe/spinachsalad.jpg", "rating": "3", "category": "Snack", "author":"itsmaboi"}




    ]

    cats = {"Vegetarian": {"recipe": vegetarian_rec},
            "Main": {"recipe": main_rec},
            "Dessert": {"recipe": dessert_rec},
            "Snack": {"recipe": snack_rec}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for r in cat_data["recipe"]:
            add_rec(c, r["title"], r["ingredients"], r["instructions"], r["description"], r["picture"], r["rating"], r["category"], r["author"])

    # for c in Category.objects.all():
    #     for r in Recipe.objects.filter(category=c):
    #         print("- {0} - {1}".format(str(c), str(r)))


def add_rec(cat, title, ingredients, instructions, description, picture, rating, category, author):
    r = Recipe.objects.get_or_create(category=cat, title=title, ingredients=ingredients, instructions=instructions, description=description, author=author)[0]
    r.picture=picture
    r.rating=rating
    r.save()
    return r


def add_cat(title):
    c = Category.objects.get_or_create(title=title) [0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting CFC population script...")
    populate()
