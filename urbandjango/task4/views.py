from django.shortcuts import render

# Create your views here.
def main_page(request):

    title = 'Главная страница'

    context = {
        'title': title,
        }

    return render(request, 'main_page.html', context)


def shop(request):

    title = 'Игры'

    games = [
        'Atomic Heart',
        'Cyberpunk 2077',
        'PayDay 2'
        ]

    context = {
        'title': title,
        'games': games
        }

    return render(request, 'shop.html', context)


def cart(request):

    title = 'Корзина'

    description = 'Извините, ваша корзина пуста'

    context = {
        'title': title,
        'desc': description
        }

    return render(request, 'cart.html', context)