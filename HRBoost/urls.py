from django.urls import path
from .views import UserInfoDetail, UserVacationList, AttendanceList

urlpatterns = [
    path("<int:pk>/", UserInfoDetail.as_view(), name="user_info_detail"),
    path("vacations", UserVacationList.as_view(), name="user_vacation_list"),
    path("attendance", AttendanceList.as_view(), name="attendance_list"),
    
]
