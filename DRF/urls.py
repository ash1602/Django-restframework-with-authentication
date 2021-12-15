from django.contrib import admin
from django.urls import path
from token_auth import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.instruList.as_view()),
    path("courses", views.courseList.as_view()),
    path("courses/<int:pk>", views.coursedetail.as_view(), name="courses-detail"),
    path("<int:pk>", views.instrudetails.as_view(), name="instructor-detail"),
    path("auth/token", obtain_auth_token, name="authtoken")


]
