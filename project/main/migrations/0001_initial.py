# Generated by Django 4.2.7 on 2023-12-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(db_index=True, max_length=10)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('content', models.TextField(blank=True, verbose_name='Информация о себе')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('contacts', models.CharField(max_length=255, verbose_name='Контакты для связи')),
                ('slug_post_one', models.SlugField(max_length=255, null=True, unique=True, verbose_name='Ваш логин')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.gender', verbose_name='Пол')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]