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
    UserInfoUpdate,
    LastAttendanceDetail,
    AttendanceUpdateDetail,
    UserInfoDetailUserID,
    UserVacationDetailUserID,
)

urlpatterns = [
    path("users/<int:pk>/", UserInfoDetail.as_view(), name="user_info_detail"),
    path(
        "userinfo/<int:user_id>/",
        UserInfoDetailUserID.as_view(),
        name="user_info_detail_by_user_id",
    ),
    path("usersupdate/<int:pk>/", UserInfoUpdate.as_view(), name="user_info_detail"),
    path("users/", UserInfoList.as_view(), name="user_info_list"),
    path("vacations/", UserVacationList.as_view(), name="user_vacation_list"),
    path("vacations/<int:pk>/", UserVacationDetail.as_view()),
    path(
        "vacationsuser/<int:user_id>/",
        UserVacationDetailUserID.as_view(),
    ),
    path("attendancelist/", AttendanceList.as_view(), name="attendance_list"),
    path(
        "attendance/<int:user_id>/",
        AttendanceDetail.as_view(),
    ),
    path(
        "attendanceupdate/<int:pk>/",
        AttendanceUpdateDetail.as_view(),
    ),
    path(
        "lastattendance/<int:user_id>/",
        LastAttendanceDetail.as_view(),
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
