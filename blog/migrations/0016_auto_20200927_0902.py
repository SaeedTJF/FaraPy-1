# Generated by Django 2.2.7 on 2020-09-27 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200927_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabs',
            name='portable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='Portable'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not confirmed'), (1, 'Confirmed')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(0, 'Primary Menu'), (1, 'Secondry Menu')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='status',
            field=models.IntegerField(choices=[(1, 'Address'), (2, 'Page'), (0, 'Category')], default=0, verbose_name='Status'),
        ),
    ]
