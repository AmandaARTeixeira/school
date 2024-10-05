from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, RegistrationViewSet, ListRegistrationStudent, ListRegistrationCourse
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename = 'students')
router.register('courses', CourseViewSet, basename = 'courses')
router.register('registration', RegistrationViewSet, basename = 'registration')

urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:pk>/registration/', ListRegistrationStudent.as_view()),    
    path('courses/<int:pk>/registration/', ListRegistrationCourse.as_view())
]