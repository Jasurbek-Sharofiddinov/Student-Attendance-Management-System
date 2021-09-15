from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User( AbstractUser ):
	# user_types
	user_type = ((1, "Admin"), (2, "Teacher"), (3, "Student"))

	user_id = models.IntegerField( primary_key=True )
	first_name = models.CharField( max_length=45 )
	last_name = models.CharField( max_length=45 )
	email = models.CharField( max_length=45 )
	contact = models.IntegerField( max_length=12 )
	user_type = models.IntegerField( default=1, choices=user_type, max_length=1 )

class Course(models.Model ):
	course_id = models.IntegerField( primary_key=True )
	course_name = models.CharField( max_length=45 )

class Subject(models.Model):
	subject_id = models.IntegerField( primary_key=True )
	subject_name = models.CharField( max_length=45 )
	course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)





class Student( models.Model ):
	admin=models.OneToOneField(User,on_delete=models.CASCADE)
	subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
	course_id=models.ForeignKey(Course,on_delete=models.CASCADE)

class Teacher( models.Model ):
	admin=models.OneToOneField(User,on_delete=models.CASCADE)
	subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)


class Attendance( models.Model ):
	present = ((1, "Present"), (0, "Absent"))


	user_id = models.IntegerField()
	subject_id = models.ForeignKey( Subject,on_delete=models.CASCADE )
	course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
	data = models.DateField()
	status = models.IntegerField( default=0, choices=present, max_length=1 )
