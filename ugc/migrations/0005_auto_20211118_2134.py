# Generated by Django 3.2.8 on 2021-11-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0004_selectedstation_selectedtransport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selectedstation',
            options={'verbose_name': 'Маршрут', 'verbose_name_plural': 'Маршруты'},
        ),
        migrations.AlterModelOptions(
            name='selectedtransport',
            options={'verbose_name': 'Транспорт', 'verbose_name_plural': 'Транспорт'},
        ),
        migrations.AlterField(
            model_name='selectedstation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время сохранения'),
        ),
        migrations.AlterField(
            model_name='selectedtransport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время сохранения'),
        ),
    ]