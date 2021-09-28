from rest_framework import serializers
from django.db import models
from .models import (
    UserRole,
    Department,
    Permission,
    Notification,
    Attendance,
    RolePermission,
    UserInfo,
    UserVacation,
)


class GetPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()
    per_id = models.IntegerField()
    role_per_id = models.IntegerField()
    has = models.BooleanField()
    field = models.CharField(max_length=40)
    description = models.TextField()
    role_name = models.CharField(max_length=15)


# class RolePermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GetPermissions
#         fields = "__all__"


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    dep_id = DepartmentSerializer()

    class Meta:
        model = UserInfo
        fields = "__all__"


class UserInfoupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


class UserVacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVacation
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserRoleSerializer(serializers.ModelSerializer):
    role = PermissionSerializer(many=True)

    class Meta:
        model = UserRole
        fields = "__all__"
