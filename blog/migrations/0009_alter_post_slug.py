# Generated by Django 4.1.6 on 2023-02-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_text_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=True, max_length=200, unique=True),
        ),
    ]