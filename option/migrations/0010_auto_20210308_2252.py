# Generated by Django 3.1.7 on 2021-03-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0009_auto_20210308_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametertype',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
