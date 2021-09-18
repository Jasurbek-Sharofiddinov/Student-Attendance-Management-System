from rest_framework import routers
from attendance import views

router=routers.DefaultRouter()

router.register(r'admins',views.AdminViewSet,basename='adminlar')
router.register(r'teachers',views.TeacherViewSet)
router.register(r'students',views.StudentViewSet)
router.register(r'courses',views.CourseViewSet)
router.register(r'subjects',views.SubjectViewSet)
router.register(r'attendance',views.AttendanceViewSet)
router.register(r'attendance-report',views.AttendanceReportViewSet)

for url in router.urls:
	print(url,'/n')