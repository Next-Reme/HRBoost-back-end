from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
from .serializers import (
    UserInfoSerializer,
    UserVacationSerializer,
    AttendanceSerializer,
)


class UserInfoDetail(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserVacationList(ListCreateAPIView):
    queryset = UserVacation.objects.all()
    serializer_class = UserVacationSerializer


class AttendanceList(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
