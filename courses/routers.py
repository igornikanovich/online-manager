from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, HomeworkViewSet, LectureViewSet, TaskViewSet, MarkViewSet, CommentViewSet


CourseRouter = DefaultRouter()
LectureRouter = DefaultRouter()
TaskRouter = DefaultRouter()
HomeworkRouter = DefaultRouter()
MarkRouter = DefaultRouter()
CommentRouter = DefaultRouter()
CourseRouter.register(r'courses', CourseViewSet)
LectureRouter.register(r'lectures', LectureViewSet)
TaskRouter.register(r'tasks', TaskViewSet)
HomeworkRouter.register(r'homework', HomeworkViewSet)
MarkRouter.register(r'mark', MarkViewSet)
CommentRouter.register(r'comments', CommentViewSet)