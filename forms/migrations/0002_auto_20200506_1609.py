# Generated by Django 2.2 on 2020-05-06 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ttile',
            new_name='title',
        ),
    ]
