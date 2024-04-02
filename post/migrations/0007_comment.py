# Generated by Django 4.1.1 on 2023-04-09 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0006_alter_post_model_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('paren', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post_model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
