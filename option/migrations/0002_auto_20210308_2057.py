# Generated by Django 3.1.7 on 2021-03-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='value',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parameter',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
