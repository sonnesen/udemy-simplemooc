# Generated by Django 2.0.7 on 2018-07-15 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100, unique=True, verbose_name='Identificador'),
            preserve_default=False,
        ),
    ]