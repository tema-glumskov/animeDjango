# Generated by Django 5.0.7 on 2024-07-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animesite', '0004_alter_animetitle_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animetitle',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
