# Generated by Django 2.2 on 2020-05-29 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djfk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='first_user',
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
