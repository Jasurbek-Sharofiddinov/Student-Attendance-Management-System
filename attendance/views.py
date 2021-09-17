from django.shortcuts import render
from rest_framework import viewsets
from attendance.models import Admin,Student,Teacher,Course,Subject,Attendance,AttendanceReport
from .serializer import AdminSerializer,TeacherSerializer,StudentSerializer,CourseSerializer,SubjectSerializer,AttendanceSerializer,AttendanceReportSerializer
# Create your views here.
class AdminViewSet(viewsets.ModelViewSet):
	queryset = Admin.objects.all()
	serializer_class = AdminSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
	queryset = Attendance.objects.all()
	serializer_class = AttendanceSerializer

class AttendanceReportViewSet(viewsets.ModelViewSet):
	queryset = AttendanceReport.objects.all()
	serializer_class = AttendanceReportSerializer


