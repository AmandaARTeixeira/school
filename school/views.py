from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationCourseSerializer, ListRegistrationStudentSerializer
from rest_framework import viewsets, generics

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListRegistrationStudent(generics.ListAPIView):
    serializer_class = ListRegistrationStudentSerializer

    def get_queryset(self):
        return Registration.objects.filter(student_id = self.kwargs['pk'])
    
class ListRegistrationCourse(generics.ListAPIView):
    serializer_class = ListRegistrationCourseSerializer

    def get_queryset(self):
        return Registration.objects.filter(course_id = self.kwargs['pk'])