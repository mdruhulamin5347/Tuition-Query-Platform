# Generated by Django 4.1.1 on 2023-05-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_post_model_catagory'),
        ('profileapp', '0004_alter_teacher_model_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_model',
            name='class_in',
            field=models.ManyToManyField(related_name='class_in', to='post.student'),
        ),
        migrations.AlterField(
            model_name='teacher_model',
            name='subject',
            field=models.ManyToManyField(related_name='subject', to='post.teacher'),
        ),
    ]
