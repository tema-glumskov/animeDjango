from django.contrib import admin
from .models import AnimeTitle, AnimeUser

# Register your models here.
admin.site.register(AnimeTitle)
admin.site.register(AnimeUser)