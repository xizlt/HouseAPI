# Generated by Django 3.1.7 on 2021-03-09 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0008_auto_20210308_1012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['-created'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='typead',
            options={'verbose_name': 'Тип объявления', 'verbose_name_plural': 'Типы объявлений'},
        ),
    ]