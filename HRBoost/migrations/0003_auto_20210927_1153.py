# Generated by Django 3.2.7 on 2021-09-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRBoost', '0002_getpermissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservacation',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='uservacation',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]