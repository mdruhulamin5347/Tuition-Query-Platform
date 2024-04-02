# Generated by Django 4.1.1 on 2023-04-05 16:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_alter_post_model_middle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_model',
            name='likes',
            field=models.ManyToManyField(related_name='set_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post_model',
            name='views',
            field=models.ManyToManyField(related_name='set_views', to=settings.AUTH_USER_MODEL),
        ),
    ]