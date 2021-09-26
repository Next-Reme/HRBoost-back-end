from django.urls import path
from .views import (
    UserInfoDetail,
    UserVacationList,
    AttendanceList,
    AttendanceDetail,
    UserInfoList,
)

urlpatterns = [
    path("users/<int:pk>/", UserInfoDetail.as_view(), name="user_info_detail"),
    path("users/", UserInfoList.as_view(), name="user_info_list"),
    path("vacations", UserVacationList.as_view(), name="user_vacation_list"),
    path("attendance", AttendanceList.as_view(), name="attendance_list"),
    path(
        "attendance/<int:pk>/", AttendanceDetail.as_view(), name="cookie_stand_detail"
    ),
]
