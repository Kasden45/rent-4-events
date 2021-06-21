# Generated by Django 3.2.2 on 2021-06-12 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Rent4Events', '0016_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='creationDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]