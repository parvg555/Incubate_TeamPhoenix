# Generated by Django 3.0.10 on 2020-10-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_pharmacist_pharmaimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
