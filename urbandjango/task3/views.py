from django.shortcuts import render

# Create your views here.
def main_page(request):

    name_page = 'Игровая платформа'

    title = 'Главная страница'

    button_main = 'Главная'

    button_shop = 'Магазин'

    button_cart = 'Корзина'

    context = {
        'name_page': name_page,
        'title': title,
        'button_main': button_main,
        'button_shop': button_shop,
        'button_cart': button_cart
        }

    return render(request, 'main_page.html', context)


def shop(request):

    name_page = 'Магазин'

    title = 'Игры'

    games = [
        'Atomic Heart',
        'Cyberpunk 2077',
        'PayDay 2'
        ]

    context = {
        'name_page': name_page,
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