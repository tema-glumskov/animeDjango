# Generated by Django 5.0.7 on 2024-07-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animesite', '0005_alter_animetitle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animetitle',
            name='image',
            field=models.ImageField(upload_to='sites/animesite/static'),
        ),
    ]
