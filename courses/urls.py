from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, HomeworkViewSet, LectureViewSet

app_name = 'Courses'

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router = DefaultRouter()
router.register(r'homeworks', HomeworkViewSet)
router = DefaultRouter()
router.register(r'lectures', LectureViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
