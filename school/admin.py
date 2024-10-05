from django.contrib import admin
from school.models import Student, Course, Registration

class ListingStudents(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'birth_date', 'phone')
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Student, ListingStudents)

class ListingCourses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code',)
    list_per_page = 20
    search_fields = ('code',)

admin.site.register(Course, ListingCourses)

class ListingRegistration(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id', 'student', 'course',)
    list_per_page = 20
    search_fields = ('code',)

admin.site.register(Registration, ListingRegistration)