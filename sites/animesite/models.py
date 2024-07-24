from django.db import models

# Create your models here.
class AnimeTitle(models.Model):
    # в Django ORM для данных существвуют собственные типы
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_link = models.URLField(null=True)
    link = models.URLField()

class AnimeUser(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    favourite_anime = list()