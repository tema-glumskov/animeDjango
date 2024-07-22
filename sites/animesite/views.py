from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': 'Артём'}
    return render(request, 'index.html', context=context)

def anime(request):
    return render(request, 'anime.html')