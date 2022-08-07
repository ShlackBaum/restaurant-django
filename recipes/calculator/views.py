from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
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
    # можете добавить свои рецепты ;)
}


def index(request, a):
    servings = request.GET.get('servings')
    if request.GET.get('servings') == None:
        servings = 1
    else:
        servings = int(request.GET.get('servings'))
    served_data = {}
    for key, value in DATA[a].items():
        served_data[key] = value * servings
    context = {
        'recipe': served_data
    }
    return render(request, 'calculator/index.html', context)