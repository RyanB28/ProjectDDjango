# Generated by Django 3.0.5 on 2020-06-04 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='BirthDay',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
