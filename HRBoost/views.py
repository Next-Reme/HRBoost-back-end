from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
from .serializers import (
    UserInfoSerializer,
    UserVacationSerializer,
    AttendanceSerializer,
)
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.decorators import api


class UserInfoList(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserInfoDetail(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserVacationList(ListCreateAPIView):
    queryset = UserVacation.objects.all()
    serializer_class = UserVacationSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AttendanceList(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class AttendanceDetail(RetrieveUpdateDestroyAPIView):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# class AttendanceDetail(RetrieveUpdateDestroyAPIView):

#     queryset = Attendance.objects.all()
#     serializer_class = AttendanceSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
