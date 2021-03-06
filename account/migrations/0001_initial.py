# Generated by Django 3.1.7 on 2021-03-06 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meter', '0002_meter_created'),
        ('application', '0002_auto_20210306_1709'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0003_auto_20210306_1849'),
        ('reservation', '0002_auto_20210306_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('ban', models.BooleanField(default=False)),
                ('ban_start', models.DateField(blank=True)),
                ('ban_end', models.DateField(blank=True)),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.ad')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.application')),
                ('indication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.indication')),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.meter')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
