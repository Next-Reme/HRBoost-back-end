from django.contrib import admin
from .models import (
    Role,
    Department,
    Permission,
    Notification,
    Attendance,
    RolePermission,
    UserInfo,
    UserVacation,
)

# Register your models here.
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Permission)
admin.site.register(Notification)
admin.site.register(Attendance)
admin.site.register(RolePermission)
admin.site.register(UserInfo)
admin.site.register(UserVacation)
