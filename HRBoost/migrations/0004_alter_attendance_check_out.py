# Generated by Django 3.2.7 on 2021-09-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRBoost', '0003_auto_20210928_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='check_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]