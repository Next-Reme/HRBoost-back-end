# Generated by Django 3.2.7 on 2021-09-27 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dep_Name", models.CharField(max_length=50)),
                (
                    "manger_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GetPermissions",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("role_id", models.IntegerField()),
                ("per_id", models.IntegerField()),
                ("role_per_id", models.IntegerField()),
                ("has", models.BooleanField()),
                ("field", models.CharField(max_length=40)),
                ("description", models.TextField()),
                ("role_name", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Permission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.CharField(max_length=40)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="UserRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role_name", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="UserVacation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("applied_date", models.DateField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("start_time", models.TimeField(default="12:00")),
                ("end_time", models.TimeField(default="12:00")),
                ("description", models.TextField()),
                ("status", models.BooleanField(default=False)),
                ("vacation_type", models.CharField(max_length=40)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("birth_date", models.DateField()),
                ("image", models.TextField(blank=True, default="user.jpg")),
                ("address", models.TextField(blank=True, null=True)),
                ("phone_num", models.CharField(blank=True, max_length=14, null=True)),
                ("gender", models.BooleanField(blank=True, null=True)),
                (
                    "social_status",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                ("job_title", models.CharField(blank=True, max_length=100, null=True)),
                ("available_leave_days", models.IntegerField(default=15)),
                ("evaluation", models.FloatField(blank=True, null=True)),
                (
                    "pre_evaluation",
                    models.FloatField(blank=True, default=0.0, null=True),
                ),
                (
                    "dep_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HRBoost.department",
                    ),
                ),
                (
                    "role_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HRBoost.userrole",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RolePermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("has", models.BooleanField()),
                (
                    "per_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HRBoost.permission",
                    ),
                ),
                (
                    "role_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HRBoost.userrole",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=60)),
                ("time", models.DateTimeField()),
                ("messahe", models.TextField()),
                ("opened", models.BooleanField(default=False)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("check_in", models.DateTimeField()),
                ("check_out", models.DateTimeField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]