# Generated by Django 3.2.8 on 2021-11-17 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0002_auto_20211117_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в соц сети'),
        ),
    ]
