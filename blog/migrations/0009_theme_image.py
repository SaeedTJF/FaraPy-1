# Generated by Django 2.2.7 on 2020-07-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200726_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='image',
            field=models.ImageField(default='theme-default-thumb.png', upload_to='themes/', verbose_name='عکس'),
        ),
    ]
