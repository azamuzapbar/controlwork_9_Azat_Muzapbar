# Generated by Django 4.2 on 2023-04-22 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
                ('description', models.CharField(max_length=200, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
