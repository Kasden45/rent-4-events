# Generated by Django 3.2.2 on 2021-05-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent4Events', '0009_auto_20210518_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='firstName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('ZA', 'Zaplanowany'), ('WT', 'W trasie'), ('ZR', 'Zrealizowany')], default='ZA', max_length=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='brand',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='carServiceTo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(blank=True, choices=[('SP', 'Sprawny'), ('WW', 'W warsztacie'), ('NI', 'Niesprawny')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(blank=True, choices=[('BU', 'Bus'), ('CI', 'Ciężarówka')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
