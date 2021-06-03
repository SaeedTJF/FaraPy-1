# Generated by Django 2.2.7 on 2020-07-05 14:50

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads/', verbose_name='تصویر')),
                ('url', models.URLField()),
                ('date', django_jalali.db.models.jDateField(verbose_name='تاریخ')),
                ('EXdate', django_jalali.db.models.jDateField(verbose_name='تاریخ اتمام تبلیغ')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'تبلیغ',
                'verbose_name_plural': 'تبلیغات',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='category/', verbose_name='تصویر')),
                ('olaviat', models.IntegerField(default=6, verbose_name='اولویت')),
                ('pcount', models.IntegerField(default=0, verbose_name='تعداد پست')),
                ('html', models.CharField(default='category.html', max_length=200, verbose_name='نام فایل دسته بندی')),
                ('htmlpost', models.CharField(default='post.html', max_length=200, verbose_name='نام فایل ادامه مطلب این دسته')),
                ('pcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='blog.Category', verbose_name='دسته بندی مادر')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'لینک',
                'verbose_name_plural': 'لینک ها',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('status', models.IntegerField(choices=[(1, 'منوی فرعی'), (0, 'منوی اصلی')], default=0, verbose_name='وضعیت')),
            ],
        ),
        migrations.CreateModel(
            name='Moshtari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=100, verbose_name='شماره همراه')),
                ('birthdate', django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ تولد')),
            ],
        ),
        migrations.CreateModel(
            name='Portable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('sex', models.IntegerField(choices=[(0, 'خانم'), (1, 'آقا')], default=0, verbose_name='جنسیت')),
                ('image', models.ImageField(upload_to='images/', verbose_name='عکس')),
                ('dpost', models.BooleanField(default=0, verbose_name='دسترسی به پست ها')),
                ('dcomment', models.BooleanField(default=0, verbose_name='دسترسی به کامنت ها')),
                ('dmultimedia', models.BooleanField(default=0, verbose_name='دسترسی به مالتی مدیا')),
                ('dvideo', models.BooleanField(default=0, verbose_name='دسترسی به ویدیو')),
                ('dcategory', models.BooleanField(default=0, verbose_name='دسترسی به دسته بندی ها')),
                ('dsafahat', models.BooleanField(default=0, verbose_name='دسترسی به صفحات اضافی')),
                ('dthemeeditor', models.BooleanField(default=0, verbose_name='ویرایش قالب')),
                ('dmenu', models.BooleanField(default=0, verbose_name='دسترسی به منوساز')),
                ('dslider', models.BooleanField(default=0, verbose_name='دسترسی به اسلایدرها')),
                ('dtaskmanager', models.BooleanField(default=0, verbose_name='دسترسی به مدیریت وظایف')),
                ('dlink', models.BooleanField(default=0, verbose_name='دسترسی به لینک ها')),
                ('dads', models.BooleanField(default=0, verbose_name='دسترسی به تبلیغات')),
                ('dform', models.BooleanField(default=0, verbose_name='دسترسی به فرم ساز')),
                ('dhavadaran', models.BooleanField(default=0, verbose_name='دسترسی به هواداران')),
                ('dkarbaran', models.BooleanField(default=0, verbose_name='دسترسی به کاربران')),
                ('dsetting', models.BooleanField(default=0, verbose_name='دسترسی به تنظیمات سایت')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userportable', to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='تصویر')),
                ('date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='عنوان')),
                ('pos', models.IntegerField(default=1, verbose_name='مکان قرارگیری')),
                ('status', models.IntegerField(choices=[(0, 'دسته بندی'), (2, 'صفحه'), (1, 'ادرس')], default=0, verbose_name='وضعیت')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Menu', verbose_name='منو')),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuu', to='blog.SubMenu', verbose_name='زیر مجموعه')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام قالب')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mozo', models.CharField(max_length=200, verbose_name='موضوع')),
                ('tozihat', models.TextField(verbose_name='توضیحات')),
                ('video', models.FileField(upload_to='video/', verbose_name='ویدیو')),
            ],
        ),
        migrations.CreateModel(
            name='SubUrl',
            fields=[
                ('submenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.SubMenu')),
                ('url', models.URLField(verbose_name='وب سابت')),
            ],
            bases=('blog.submenu',),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_date', django_jalali.db.models.jDateField(verbose_name='تاریخ ورود')),
                ('out_date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ خروج')),
                ('in_time', models.TimeField(verbose_name='ساعت ورود')),
                ('out_time', models.TimeField(null=True, verbose_name='ساعت خروج')),
                ('status', models.IntegerField(choices=[(1, 'خارج از وظیفه'), (0, 'در حال وظیفه')], default=0, verbose_name='وضعیت')),
                ('portable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='نویسنده')),
            ],
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='فورم')),
            ],
        ),
        migrations.CreateModel(
            name='Task_manegar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('sharh', models.TextField(verbose_name='شرح')),
                ('cretat_time', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ شروع')),
                ('end_time', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ پایان')),
                ('status', models.IntegerField(choices=[(1, 'برای آینده'), (0, 'در حال انجام'), (3, 'انجام شده')], default=0, verbose_name='وضعیت')),
                ('portable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='نویسنده')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persian_title', models.CharField(max_length=200, verbose_name='عنوان فارسی')),
                ('engilsh_title', models.CharField(max_length=200, verbose_name='english title')),
                ('introduction', models.TextField(verbose_name='معرفی کوتاه')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('instagram', models.URLField(blank=True, default='instagram.com/', null=True, verbose_name='اینستاگرام')),
                ('facebook', models.URLField(blank=True, default='facebook.com/', null=True, verbose_name='فیس بوک')),
                ('linkedin', models.URLField(blank=True, default='linkedin.com/', null=True, verbose_name='لینکدین')),
                ('twitter', models.URLField(blank=True, default='twitter.com/', null=True, verbose_name='توییتر')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='واتس آپ')),
                ('telgram', models.URLField(blank=True, null=True, verbose_name='تلگرام')),
                ('aboutus', models.TextField(null=True, verbose_name='درباره ما')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('logo', models.FileField(upload_to='logo/', verbose_name='لوگو')),
                ('city', models.CharField(default='tehran', max_length=200, verbose_name='شهر')),
                ('tel_no', models.IntegerField(verbose_name='شماره تماس')),
                ('api', models.CharField(max_length=200, null='True', verbose_name='api kavenegar')),
                ('createdate', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ شروع لایسنس')),
                ('expdate', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ اتمام لایسنس')),
                ('form', models.BooleanField(default=0, verbose_name='فرم')),
                ('ads', models.BooleanField(default=0, verbose_name='تبلیغات')),
                ('protable', models.BooleanField(default=0, verbose_name='کاربران')),
                ('moshtari', models.BooleanField(default=0, verbose_name='باشگاه مشترکین')),
                ('video', models.BooleanField(default=0, verbose_name='ویدیو')),
                ('safahat', models.BooleanField(default=0, verbose_name='صفحات')),
                ('task_manegar', models.BooleanField(default=0, verbose_name='مدیریت وظایف')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Theme', verbose_name='قالب')),
            ],
        ),
        migrations.CreateModel(
            name='Safahat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
                ('view', models.IntegerField(default=0, verbose_name='بازدید')),
                ('created_date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ')),
                ('image', models.ImageField(upload_to='post/', verbose_name='تصویر')),
                ('html', models.CharField(default='page.html', max_length=200, verbose_name='نام فایل قالب')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Portable', verbose_name='نویسنده')),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='فرم')),
            ],
            options={
                'verbose_name': 'صفحات اضافی',
                'verbose_name_plural': 'صفحات اضافی',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('demo', models.TextField(verbose_name='توضیح کوتاه')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
                ('view', models.IntegerField(default=0, verbose_name='بازدید')),
                ('sartitr', models.BooleanField(default=0, verbose_name='تیتر')),
                ('com', models.BooleanField(default=0, verbose_name='کامنت باز باشد؟')),
                ('created_date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ')),
                ('status', models.IntegerField(choices=[(0, 'پیش نویس'), (1, 'انتشار')], default=0, verbose_name='وضعیت ')),
                ('image', models.ImageField(upload_to='post/', verbose_name='تصویر')),
                ('barchasb', models.TextField(blank=True, null=True, verbose_name='برچسب')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='blog.Portable', verbose_name='نویسنده')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='دسته بندی')),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='فرم')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'مطالب',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='به روز رسانی')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
                ('created_date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ')),
                ('status', models.IntegerField(choices=[(0, 'پیش نویس'), (1, 'انتشار')], default=0, verbose_name='وضعیت')),
                ('image', models.ImageField(upload_to='multi/', verbose_name='تصویر')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'چندرسانه ای',
                'verbose_name_plural': 'چند رسانه ای',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('type', models.CharField(choices=[('email', 'ایمیل'), ('number', 'عدد'), ('password', 'پسورد'), ('text', 'متن')], default='text', max_length=10, verbose_name='نوع فیلد')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='فورم')),
            ],
        ),
        migrations.CreateModel(
            name='Copen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copeni', models.IntegerField(default=0, verbose_name='میزان درصد کوپن')),
                ('moshtari', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Moshtari', verbose_name='مشتری')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('text', models.TextField(verbose_name='توضیح ')),
                ('date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ')),
                ('status', models.IntegerField(choices=[(0, 'تائید نشده'), (1, 'تائید شد')], default=0, verbose_name='وضعیت')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='AnswerTextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='عنوان')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Answer', verbose_name='جواب')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.TextField', verbose_name='فورم')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='عنوان')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Answer', verbose_name='جواب')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Field', verbose_name='فورم')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Form', verbose_name='فورم'),
        ),
        migrations.CreateModel(
            name='SubPage',
            fields=[
                ('submenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.SubMenu')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Safahat', verbose_name='صفحات')),
            ],
            bases=('blog.submenu',),
        ),
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('submenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.SubMenu')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='دسته بندی')),
            ],
            bases=('blog.submenu',),
        ),
    ]
