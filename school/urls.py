from django.contrib import admin
from django.urls import path
from school.views import students

urlpatterns = [
    path('students/', students, name='students')
]