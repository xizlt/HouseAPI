# Generated by Django 3.1.7 on 2021-03-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0003_auto_20210308_0933'),
        ('account', '0003_auto_20210306_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ad',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='application',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='indication',
        ),
        migrations.AddField(
            model_name='profile',
            name='indication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meter.indication'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='meter',
        ),
        migrations.AddField(
            model_name='profile',
            name='meter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meter.meter'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.status'),
        ),
    ]
