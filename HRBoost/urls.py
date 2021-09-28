from django.urls import path
from .views import (
    UserInfoDetail,
    UserVacationList,
    AttendanceList,
    AttendanceDetail,
    UserInfoList,
    RolePermissionList,
    UserRoleper,
    UserVacationDetail,
)

urlpatterns = [
    path("users/<int:pk>/", UserInfoDetail.as_view(), name="user_info_detail"),
    path("users/", UserInfoList.as_view(), name="user_info_list"),
    path("vacations/", UserVacationList.as_view(), name="user_vacation_list"),
    path(
        "vacations/<int:pk>/", UserVacationDetail.as_view(), name="user_vacation_list"
    ),
    path("attendancelist/", AttendanceList.as_view(), name="attendance_list"),
    path(
        "attendance/<int:user_id>/",
        AttendanceDetail.as_view(),
        name="cookie_stand_detail",
    ),
    path(
        "rolepermission/<int:role_id>/",
        RolePermissionList.as_view(),
        name="role_permission_list",
    ),
    path(
        "userroleper/",
        UserRoleper.as_view(),
    ),
]
