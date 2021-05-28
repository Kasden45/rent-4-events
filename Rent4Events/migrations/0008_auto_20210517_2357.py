# Generated by Django 3.2.2 on 2021-05-17 21:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rent4Events', '0007_alter_driver_employmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='ClientUser'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='employmentDate',
            field=models.DateField(default=datetime.datetime(2021, 5, 17, 21, 57, 9, 921748, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='DriverUser'),
        ),
    ]