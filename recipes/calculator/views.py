from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cake': {
        'шоколад, плитка': 0.5,
        'сахар, ч.л': 1,
        'сметана, ч.л': 0.5,
        'клубника, шт': 5
    },
    'meatballs': {
        'фарш, г': 100,
        'рис, г': 20,
        'мука, ст': 0.3,
        'соль, ч.л.': 0.5
    }
}


def calculator_recipe(request, recipe):

    if recipe in DATA:
        ingredients = DATA[recipe]
        servings = request.GET.get('servings', None)

        if servings:
            result = dict()
            for item, value in ingredients.items():
                new_value = value * int(servings)
                result[item] = new_value
            context = {
                'recipe_name': recipe,
                'recipe': result
            }
        else:
            context = {
                'recipe_name': recipe,
                'recipe': ingredients
            }

    else:
        context = None

    return render(request, template_name='calculator/index.html', context=context)


def home(request):

    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, template_name='calculator/home.html', context=context)
