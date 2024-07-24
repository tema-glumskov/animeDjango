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
        user = AnimeUser.objects.filter(login=login).first()
        user.favourite_anime.append(title)
        user.save()
        print(user.favourite_anime)
        print('Угабуга!')
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