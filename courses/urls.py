from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, HomeworkViewSet, LectureViewSet, TaskViewSet, MarkViewSet, CommentViewSet

app_name = 'Courses'

CourseRouter = DefaultRouter()
LectureRouter = DefaultRouter()
TaskRouter = DefaultRouter()
HomeworkRouter = DefaultRouter()
MarkRouter = DefaultRouter()
CommentRouter = DefaultRouter()
CourseRouter.register(r'courses', CourseViewSet)
LectureRouter.register(r'lectures', LectureViewSet)
TaskRouter.register(r'tasks', TaskViewSet)
HomeworkRouter.register(r'homeworks', HomeworkViewSet)
MarkRouter.register(r'marks', MarkViewSet)
CommentRouter.register(r'comments', CommentViewSet)

urlpatterns = [
    url(r'', include(CourseRouter.urls)),
    path(r'courses/<int:course_id>/', include(LectureRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/', include(TaskRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/', include(HomeworkRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/homeworks/<int:homework_id>/',
         include(MarkRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/homeworks/<int:homework_id>/'
         r'marks/<int:mark_id>/', include(CommentRouter.urls)),
]
