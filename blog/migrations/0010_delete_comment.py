# Generated by Django 4.1.6 on 2023-02-23 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
