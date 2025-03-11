# Generated by Django 5.1.6 on 2025-03-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='about',
        ),
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='recipe',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='tips',
            field=models.TextField(default=''),
        ),
    ]
