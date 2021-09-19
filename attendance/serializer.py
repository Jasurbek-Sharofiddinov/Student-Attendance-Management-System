from rest_framework import serializers
from . import models
from .models import Admin,Student,Teacher,Course,Subject,Attendance,AttendanceReport

class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model=Admin
		fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):

	class Meta:
		model=Teacher
		fields='__all__'

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model=Student
		fields='__all__'

class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model=Course
		fields='__all__'


class SubjectSerializer(serializers.ModelSerializer):

	class Meta:
		model=Subject
		fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):

	class Meta:
		model=Attendance
		fields='__all__'

class AttendanceReportSerializer(serializers.ModelSerializer):

	class Meta:
		model=AttendanceReport
		fields='__all__'
