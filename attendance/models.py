from django.contrib.auth.models import AbstractUser

from django.db import models


# Create your models here.

# class CustomUser(AbstractUser):
# 	user_type_data=((1,"Admin"),(2,"Teacher"),(3,"Student"))
# 	user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
class Admin(models.Model):
	# user_types
	a_id=models.AutoField(primary_key=True)
#	admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	name = models.CharField( max_length=255 )
	email = models.CharField( max_length=45 )
	password = models.CharField( max_length=45 )
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

	def __str__(self):
		return self.name

class Teacher( models.Model ):
	teacher_id=models.AutoField(primary_key=True)
#	admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	email=models.CharField(max_length=45)
	password=models.CharField(max_length=45)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	def __str__(self):
		return self.name

class Course(models.Model ):
	course_id = models.AutoField(primary_key=True)
	course_name = models.CharField(max_length=45)
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now_add=True )
	objects = models.Manager()

	def __str__(self):
		return self.course_name


class Subject(models.Model):
	subject_id = models.AutoField(primary_key=True )
	subject_name = models.CharField( max_length=45 )
	course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now_add=True )
	objects = models.Manager()

	def __str__(self):
		return self.subject_name


class Student(models.Model):

	student_id=models.AutoField(primary_key=True)
#	admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	name = models.CharField( max_length=255 )
	email = models.CharField( max_length=45 )
	password = models.CharField( max_length=45 )
	contact_n=models.CharField(max_length=12)
	profile_pic=models.FileField(blank=True)
	course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now_add=True )
	objects = models.Manager()

	def __str__(self):
		return self.name

class Attendance( models.Model ):
	attendance_id = models.AutoField(primary_key=True)
	subject_id = models.ForeignKey( Subject,on_delete=models.CASCADE )
	data = models.DateField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	def __str__(self):
		return self.attendance_id

class AttendanceReport(models.Model):
	report_id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
	attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
	status=models.BooleanField(default=False)
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now_add=True )
	objects = models.Manager()

	def __str__(self):
		return self.report_id