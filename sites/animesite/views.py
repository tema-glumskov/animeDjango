from django.shortcuts import render, redirect
from django.contrib import messages
from animesite.models import AnimeTitle, AnimeUser

# переменные сайта
locked = True

# Create your views here.
def index(request):
    global locked
    global login
    context = {'name': 'Артём'}
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        if login == 'admin' and password == '1234':
            locked = False
            return redirect('anime')
        elif AnimeUser.objects.filter(login=login, password=password).exists():
            locked = False
            return redirect('anime')
    return render(request, 'index.html', context=context)

def anime(request):
    global locked
    global login
    context = {'anime_titles': AnimeTitle.objects.all()}
    if request.method == 'POST':
        title = request.POST.get('title')
        user = AnimeUser.objects.get(login=login)
        if title not in user.favourite_anime.split('\n'):
            user.favourite_anime += f'{title}\n'
            user.save()
        else:
            print('Такое аниме уже добавлено в избранное!')
    if locked:
        return redirect('https://youtu.be/dQw4w9WgXcQ?si=N5_ZSmfxseh59c3k')
    return render(request, 'anime.html', context=context)

def manga(request):
    return render(request, 'manga.html')

def register(request):
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        if not(AnimeUser.objects.filter(login=login).exists()):
            AnimeUser.objects.create(login=login, password=password)
            messages.success(request, 'Регистрация прошла успешно!')
        else:
            messages.success(request, 'Такой пользователь уже существует!')
    return render(request, 'register.html')


def account(request):
    global locked
    global login
    if locked:
        return redirect('https://youtu.be/dQw4w9WgXcQ?si=N5_ZSmfxseh59c3k')
    user = AnimeUser.objects.get(login=login)
    context = {
        'username': user.login, 
        'favourite_anime': '\n'.join(set(user.favourite_anime.split('\n')))
        }
    if request.method == 'POST':
        if 'logout' in request.POST:
            print('Вы вышлИ!')
            locked = True
            return redirect('index')
        elif 'delete' in request.POST:
            anime_list = user.favourite_anime.split('\n')
            anime_list.remove(request.POST.get('title'))
            user.favourite_anime = '\n'.join(anime_list)
            user.save()
            return redirect('account')

    return render(request, 'account.html', context=context)