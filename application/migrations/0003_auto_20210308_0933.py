# Generated by Django 3.1.7 on 2021-03-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210308_0933'),
        ('application', '0002_auto_20210306_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]
