from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


users = ['tom', 'ivan', 'mary']


# Create your views here.
def sign_up_by_html(request):
    context = {
        'info': {},
        'info_user': {
            'username': '',
            'password': '',
            'repeat_password': '',
            'age': ''
        }
    }
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        context['info_user']['username'] = username
        context['info_user']['password'] = password
        context['info_user']['repeat_password'] = repeat_password
        context['info_user']['age'] = age

        if (username not in users and
            password == repeat_password and
            int(age) >= 18):
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}')

        elif password != repeat_password:
            context['info']['error'] = 'Пароли не совподают'
            return render(request, 'registration_page.html', context)

        elif int(age) <= 18:
            context['info']['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', context)

        elif username in users:
            context['info']['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context)

    return render(request, 'registration_page.html')



def sign_up_by_django(request):

    context = {
        'info': {},
        'info_user': {
            'username': '',
            'password': '',
            'repeat_password': '',
            'age': ''
        }
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            print('Form is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            context['info_user']['username'] = username
            context['info_user']['password'] = password
            context['info_user']['repeat_password'] = repeat_password
            context['info_user']['age'] = age

            if (username not in users and
                password == repeat_password and
                int(age) >= 18):
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}')

            elif password != repeat_password:
                context['info']['error'] = 'Пароли не совподают'
                return render(request, 'registration_page.html', context)

            elif int(age) <= 18:
                context['info']['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)

            elif username in users:
                context['info']['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)
    else:
        print('Form is not valid')
        form = UserRegister()

    context['form'] = form

    return render(request, 'registration_page.html', context)