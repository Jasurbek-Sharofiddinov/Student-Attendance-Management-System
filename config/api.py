from rest_framework import routers
from attendance import views

router=routers.DefaultRouter()

router.register(r'admins',views.AdminViewSet)
router.register(r'teachers',views.TeacherViewSet)
router.register(r'students',views.StudentViewSet)
router.register(r'courses',views.CourseViewSet)
router.register(r'subjects',views.SubjectViewSet)
router.register(r'attendance',views.AttendanceViewSet)
router.register(r'attendance-report',views.AttendanceReportViewSet)
router.register(r'admins',views.AdminViewSet)