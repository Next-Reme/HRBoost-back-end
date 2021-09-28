# Generated by Django 3.2.7 on 2021-09-28 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HRBoost', '0002_alter_rolepermission_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrole',
            name='role',
            field=models.ManyToManyField(through='HRBoost.RolePermission', to='HRBoost.Permission'),
        ),
        migrations.AlterField(
            model_name='rolepermission',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRBoost.userrole'),
        ),
    ]