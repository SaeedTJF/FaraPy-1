# Generated by Django 2.2.7 on 2020-07-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200706_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(1, 'منوی فرعی'), (0, 'منوی اصلی')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='status',
            field=models.IntegerField(choices=[(0, 'دسته بندی'), (1, 'ادرس'), (2, 'صفحه')], default=0, verbose_name='وضعیت'),
        ),
    ]
