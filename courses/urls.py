from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, HomeworkViewSet, LectureViewSet, TaskViewSet, MarkViewSet

app_name = 'Courses'

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
LectureRouter = DefaultRouter()
LectureRouter.register(r'lectures', LectureViewSet)
TaskRouter = DefaultRouter()
TaskRouter.register(r'tasks', TaskViewSet)
HomeworkRouter = DefaultRouter()
HomeworkRouter.register(r'homework', HomeworkViewSet)
MarkRouter = DefaultRouter()
MarkRouter.register(r'mark', MarkViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    path(r'courses/<int:course_id>/', include(LectureRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/', include(TaskRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/', include(HomeworkRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/homework/',
         include(MarkRouter.urls)),
]

