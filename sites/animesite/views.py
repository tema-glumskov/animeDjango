from django.shortcuts import render, redirect
from animesite.models import AnimeTitle

# переменные сайта
locked = True

# Create your views here.
def index(request):
    global locked
    context = {'name': 'Артём'}
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        if login == 'admin' and password == '1234':
            locked = False
            return redirect('anime')
    return render(request, 'index.html', context=context)

def anime(request):
    global locked
    context = {'anime_titles': AnimeTitle.objects.all()}

    if locked:
        return redirect('https://youtu.be/dQw4w9WgXcQ?si=N5_ZSmfxseh59c3k')
    return render(request, 'anime.html', context=context)

def manga(request):
    return render(request, 'manga.html')

def register(request):
    return render(request, 'register.html')