from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename = 'students')
router.register('courses', CourseViewSet, basename = 'courses')

urlpatterns = [
    path('', include(router.urls)),
]