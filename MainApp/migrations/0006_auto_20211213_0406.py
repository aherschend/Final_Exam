# Generated by Django 3.0.5 on 2021-12-13 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_photo',
            new_name='header_image',
        ),
    ]
