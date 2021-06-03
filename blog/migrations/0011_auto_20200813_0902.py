# Generated by Django 2.2.7 on 2020-08-13 04:32

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200812_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
        migrations.AlterModelOptions(
            name='multimedia',
            options={'ordering': ['-created_date'], 'verbose_name': 'Multimedia', 'verbose_name_plural': 'Multimedia'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='safahat',
            options={'ordering': ['-created_date'], 'verbose_name': 'Pages', 'verbose_name_plural': 'Pages'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Slider', 'verbose_name_plural': 'Sliders'},
        ),
        migrations.AlterField(
            model_name='ads',
            name='EXdate',
            field=models.DateField(verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='date',
            field=models.DateField(verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='answerfield',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Answer', verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='answerfield',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Field', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='answerfield',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='answertextfield',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Answer', verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='answertextfield',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.TextField', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='answertextfield',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='html',
            field=models.CharField(default='category.html', max_length=200, verbose_name='Category file name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='htmlpost',
            field=models.CharField(default='post.html', max_length=200, verbose_name='File name Read more of this category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not confirmed'), (1, 'Confirmed')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Text '),
        ),
        migrations.AlterField(
            model_name='copen',
            name='copeni',
            field=models.IntegerField(default=0, verbose_name='Percentage of coupons'),
        ),
        migrations.AlterField(
            model_name='copen',
            name='moshtari',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Moshtari', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='field',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='field',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('email', 'Email'), ('number', 'Number'), ('password', 'Password'), ('text', 'Text')], default='text', max_length=10, verbose_name='Type of field'),
        ),
        migrations.AlterField(
            model_name='form',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='links',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.IntegerField(choices=[(0, 'Primary Menu'), (1, 'Secondry Menu')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='moshtari',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='moshtari',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='moshtari',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='moshtari',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='created_date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='image',
            field=models.ImageField(upload_to='multi/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Update'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dads',
            field=models.BooleanField(default=1, verbose_name='Access to Ads'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dcategory',
            field=models.BooleanField(default=1, verbose_name='Access to Categories'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dcomment',
            field=models.BooleanField(default=1, verbose_name='Access to Comments'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dform',
            field=models.BooleanField(default=1, verbose_name='Access to FormMaker'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dhavadaran',
            field=models.BooleanField(default=1, verbose_name='Access to Customers'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dkarbaran',
            field=models.BooleanField(default=1, verbose_name='Access to Users'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dlink',
            field=models.BooleanField(default=1, verbose_name='Access to Links'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dmenu',
            field=models.BooleanField(default=1, verbose_name='Access to MenuMaker'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dmultimedia',
            field=models.BooleanField(default=1, verbose_name='Access to Multimedia'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dpost',
            field=models.BooleanField(default=1, verbose_name='Access to Posts'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dsafahat',
            field=models.BooleanField(default=1, verbose_name='Access to Pages'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dsetting',
            field=models.BooleanField(default=1, verbose_name='Access to Setting'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dslider',
            field=models.BooleanField(default=1, verbose_name='Access to Sliders'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dtaskmanager',
            field=models.BooleanField(default=1, verbose_name='Access to TaskManager'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dthemeeditor',
            field=models.BooleanField(default=1, verbose_name='Edit Format'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='dvideo',
            field=models.BooleanField(default=1, verbose_name='Access to Video'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='image',
            field=models.ImageField(default='user.png', upload_to='images/', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (0, 'Female')], default=0, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='portable',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userportable', to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='blog.Portable', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='barchasb',
            field=models.TextField(blank=True, null=True, verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='com',
            field=models.BooleanField(default=0, verbose_name='Users can comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='demo',
            field=models.TextField(verbose_name='Short explanation'),
        ),
        migrations.AlterField(
            model_name='post',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sartitr',
            field=models.BooleanField(default=0, verbose_name='Triggear'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, verbose_name='Status '),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0, verbose_name='View'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='created_date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='html',
            field=models.CharField(default='page.html', max_length=200, verbose_name='Format file name'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='image',
            field=models.ImageField(upload_to='post/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='safahat',
            name='view',
            field=models.IntegerField(default=0, verbose_name='View'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=models.TextField(null=True, verbose_name='About us'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='ads',
            field=models.BooleanField(default=1, verbose_name='Ads'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='api',
            field=models.CharField(max_length=200, null=True, verbose_name='Api kavenegar'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='city',
            field=models.CharField(default='tehran', max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='createdate',
            field=models.DateField(null=True, verbose_name='License create date'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='expdate',
            field=models.DateField(null=True, verbose_name='License expiration date'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.URLField(blank=True, default='facebook.com/', null=True, verbose_name='Face Book'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='form',
            field=models.BooleanField(default=1, verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.URLField(blank=True, default='instagram.com/', null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='introduction',
            field=models.TextField(verbose_name='Short introduction'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='linkedin',
            field=models.URLField(blank=True, default='linkedin.com/', null=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.FileField(default='logo.jpg', upload_to='logo/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='moshtari',
            field=models.BooleanField(default=1, verbose_name='Customers club'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='protable',
            field=models.BooleanField(default=1, verbose_name='Users'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='safahat',
            field=models.BooleanField(default=1, verbose_name='Pages'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='task_manegar',
            field=models.BooleanField(default=1, verbose_name='Task manager'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='tel_no',
            field=models.IntegerField(null=True, verbose_name='Tel'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='telgram',
            field=models.URLField(blank=True, null=True, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Theme', verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.URLField(blank=True, default='twitter.com/', null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='video',
            field=models.BooleanField(default=1, verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='Watsapp'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='subcat',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='pos',
            field=models.IntegerField(default=1, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='status',
            field=models.IntegerField(choices=[(0, 'Category'), (1, 'Address'), (2, 'Page')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuu', to='blog.SubMenu', verbose_name='SubMenu'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='subpage',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Safahat', verbose_name='Pages'),
        ),
        migrations.AlterField(
            model_name='suburl',
            name='url',
            field=models.URLField(verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='created_time',
            field=models.DateField(null=True, verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='end_time',
            field=models.DateField(null=True, verbose_name='Finish date'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='portable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='sharh',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='status',
            field=models.IntegerField(choices=[(3, 'Complete!'), (0, 'Incomplete!'), (1, 'Completing')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='task_manegar',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='image',
            field=models.ImageField(default='theme-default-thumb.png', upload_to='themes/', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Format name'),
        ),
        migrations.AlterField(
            model_name='time',
            name='in_date',
            field=models.DateField(verbose_name='Login date'),
        ),
        migrations.AlterField(
            model_name='time',
            name='in_time',
            field=models.TimeField(verbose_name='Clock-in'),
        ),
        migrations.AlterField(
            model_name='time',
            name='out_date',
            field=models.DateField(null=True, verbose_name='Logout date'),
        ),
        migrations.AlterField(
            model_name='time',
            name='out_time',
            field=models.TimeField(null=True, verbose_name='Clock-out'),
        ),
        migrations.AlterField(
            model_name='time',
            name='portable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='time',
            name='status',
            field=models.IntegerField(choices=[(1, 'Out of Duty'), (0, 'On Duty')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='video',
            name='mozo',
            field=models.CharField(max_length=200, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tozihat',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/', verbose_name='Video'),
        ),
    ]
