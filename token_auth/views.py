from .models import Courses, Instructor
from rest_framework import generics
from .serializers import InstruSerializer, CourseSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)


class adminpermissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return True
        if request.method == "PUT" or request.method == "POST" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False


class instruList(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstruSerializer


class courseList(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, adminpermissions]
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class coursedetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class instrudetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstruSerializer
