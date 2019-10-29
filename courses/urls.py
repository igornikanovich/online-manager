from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, HomeworkViewSet, LectureViewSet, TaskViewSet

app_name = 'Courses'

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
lectureRouter = DefaultRouter()
lectureRouter.register(r'lectures', LectureViewSet)
taskRouter = DefaultRouter()
taskRouter.register(r'tasks', TaskViewSet)



urlpatterns = [
    url(r'', include(router.urls)),
    path(r'courses/<int:course_id>/', include(lectureRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/', include(taskRouter.urls)),
]

