from rest_framework import serializers
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


class UserInfoSerializer(serializers.ModelSerializer):
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
        model = RolePermission
        fields = ("id", "per_id")


class Serializer(serializers.ModelSerializer):
    roles = PermissionSerializer()

    class Meta:
        model = UserRole
        fields = ("role_name", "per_id", "id")
