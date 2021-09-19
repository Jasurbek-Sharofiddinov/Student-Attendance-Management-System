from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from attendance.models import Admin,Student,Teacher,Course,Subject,Attendance,AttendanceReport
from .serializer import AdminSerializer,TeacherSerializer,StudentSerializer,CourseSerializer,SubjectSerializer,AttendanceSerializer,AttendanceReportSerializer

# list/create/retrive/update/partial_update/destroy
class AdminViewSet(viewsets.ViewSet):
	def list(self,request):
		queryset=Admin.objects.all()
		serializer=AdminSerializer(queryset,many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=AdminSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class AdminViewSet(viewsets.ModelViewSet):
# 	queryset = Admin.objects.all()
# 	serializer_class = AdminSerializer

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


