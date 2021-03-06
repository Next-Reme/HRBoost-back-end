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
    Blog,
)
from .serializers import (
    UserInfoSerializer,
    UserVacationSerializer,
    AttendanceSerializer,
    RolePermissionSerializer,
    PermissionSerializer,
    UserRoleSerializer,
    GetPermissions,
    DepartmentSerializer,

    BlogSerializer,

    UserInfoupdateSerializer,

)

# from .permissions import IsOwnerOrReadOnly

# from django.contrib.auth.decorators import api


class UserInfoList(ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserInfoDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class UserInfoDetailUserID(ListCreateAPIView):

    serializer_class = UserInfoupdateSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return UserInfo.objects.filter(user_id=user_id)

    # permission_classes = (IsOwnerOrReadOnly,)


class UserInfoUpdate(RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoupdateSerializer


class UserVacationList(ListCreateAPIView):
    queryset = UserVacation.objects.all()
    serializer_class = UserVacationSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class UserVacationDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserVacation.objects.all()
    serializer_class = UserVacationSerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class UserVacationDetailUserID(ListCreateAPIView):
    serializer_class = UserVacationSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return UserVacation.objects.filter(user_id=user_id)


class AttendanceList(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = IsOwnerOrReadOnly


class AttendanceDetail(ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        username = self.kwargs["user_id"]
        return Attendance.objects.filter(user_id=username)


class AttendanceUpdateDetail(RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class LastAttendanceDetail(ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        last = Attendance.objects.filter(user_id=user_id).order_by("-id")
        return last


class RolePermissionList(ListCreateAPIView):
    serializer_class = RolePermissionSerializer

    def get_queryset(self):
        role_id = self.kwargs["role_id"]
        return RolePermission.objects.filter(role_id=role_id)


class UserRoleper(ListCreateAPIView):
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()

    # def get_queryset(self):
    #     # role_id = self.kwargs["role_id"]
    #     return RolePermission.objects.all()


class Blog(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


# class AdminRolePermissionList(ListCreateAPIView):

#     queryset = RolePermission.objects.filter(role_id="1")
#     serializer_class = RolePermissionSerializer
# permission_classes = (IsOwnerOrReadOnly,)


# class UserRolePermissionList(ListCreateAPIView):

#     queryset = RolePermission.objects.filter(role_id="2")
#     serializer_class = RolePermissionSerializer
# permission_classes = (IsOwnerOrReadOnly,)


# class RolePermissionList(ListCreateAPIView):

#     queryset = GetPermissions.objects.raw(
#         "select * from UserInfo LEFT JOIN HRBoost_userrole ON HRBoost_userinfo.role_id_id = userrole.id LEFT JOIN rolepermission ON userrole.id = rolepermission.role_id_id"
#     )
#     serializer_class = RolePermissionSerializer
# permission_classes = (IsOwnerOrReadOnly,)
