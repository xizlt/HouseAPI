# Generated by Django 3.1.7 on 2021-03-09 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20210308_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-created'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='typeapplication',
            options={'verbose_name': 'Тип заявки', 'verbose_name_plural': 'Типы заявок'},
        ),
    ]
