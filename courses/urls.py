from django.conf.urls import url, include
from django.urls import path

from .routers import *

app_name = 'Courses'

urlpatterns = [
    url(r'', include(CourseRouter.urls)),
    path(r'courses/<int:course_id>/', include(LectureRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/', include(TaskRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/', include(HomeworkRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/homework/<int:homework_id>/',
         include(MarkRouter.urls)),
    path(r'courses/<int:course_id>/lectures/<int:lecture_id>/tasks/<int:task_id>/homework/<int:homework_id>/'
         r'mark/<int:mark_id>/', include(CommentRouter.urls)),
]
