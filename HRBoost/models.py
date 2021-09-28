from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class UserRole(models.Model):

    role_name = models.CharField(max_length=15)

    def __str__(self):
        return self.role_name


class Department(models.Model):
    manger_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False, blank=False
    )
    dep_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_Name


class UserInfo(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False, blank=False
    )
    dep_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=False, blank=False
    )
    role_id = models.ForeignKey(
        UserRole, on_delete=models.CASCADE, null=False, blank=False
    )
    birth_date = models.DateField()
    image = models.TextField(default="user.jpg", blank=True)
    address = models.TextField(null=True, blank=True)
    phone_num = models.CharField(max_length=14, null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)
    social_status = models.CharField(max_length=60, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    available_leave_days = models.IntegerField(default=15)
    evaluation = models.FloatField(null=True, blank=True)
    pre_evaluation = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return str(self.user_id)


class UserVacation(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False, blank=False
    )
    applied_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(default="12:00")
    end_time = models.TimeField(default="12:00")
    description = models.TextField()
    status = models.BooleanField(default=False)
    vacation_type = models.CharField(max_length=40)

    def __str__(self):
        return self.vacation_type


class Attendance(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False, blank=False
    )
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return str(self.user_id)


class Notification(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False, blank=False
    )
    title = models.CharField(max_length=60)
    time = models.DateTimeField()
    messahe = models.TextField()
    opened = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# class Role(models.Model):

#     role_name = models.CharField(max_length=15)

#     def __str__(self):
#         return self.role_name


class Permission(models.Model):

    field = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.field


class RolePermission(models.Model):

    role_id = models.ForeignKey(
        UserRole, on_delete=models.CASCADE, null=False, blank=False
    )
    per_id = models.ForeignKey(
        Permission, on_delete=models.CASCADE, null=False, blank=False
    )
    has = models.BooleanField()

    def __str__(self):
        return str(self.per_id)
