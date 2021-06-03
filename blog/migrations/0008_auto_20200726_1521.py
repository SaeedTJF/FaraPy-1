# Generated by Django 2.2.7 on 2020-07-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200726_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(1, 'تائید شد'), (0, 'تائید نشده')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(0, 'منوی اصلی'), (1, 'منوی فرعی')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='sex',
            field=models.IntegerField(choices=[(0, 'خانم'), (1, 'آقا')], default=0, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='status',
            field=models.IntegerField(choices=[(2, 'صفحه'), (1, 'ادرس'), (0, 'دسته بندی')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='sharh',
            field=models.TextField(blank=True, null=True, verbose_name='شرح'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='status',
            field=models.IntegerField(choices=[(1, 'درحال انجام'), (3, 'انجام شده'), (0, 'انجام نشده')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='time',
            name='status',
            field=models.IntegerField(choices=[(1, 'خارج از وظیفه'), (0, 'در حال وظیفه')], default=0, verbose_name='وضعیت'),
        ),
    ]
