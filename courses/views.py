from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.permissions import IsTeacher, IsStudent, IsAuthor
from .models import Course, Homework, Lecture, Task, Mark, Comment
from .serializers import CourseSerializer, CourseReadSerializer, TaskSerializer, TaskReadSerializer, \
    LectureSerializer, LectureReadSerializer, HomeworkReadSerializer, HomeworkSerializer, MarkReadSerializer, \
    MarkSerializer, CommentReadSerializer, CommentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a course.
    """
    queryset = Course.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsTeacher],
        'update': [IsAuthenticated, IsTeacher],
        'partial_update': [IsAuthenticated, IsTeacher],
        'destroy': [IsAuthenticated, IsTeacher],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return CourseReadSerializer if self.request.method == 'GET' else CourseSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Course.objects.all()
        if user.user_type == 1:
            return Course.objects.filter(teachers=user)
        else:
            return Course.objects.filter(students=user)


class LectureViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a lecture.
    """
    queryset = Lecture.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsTeacher],
        'update': [IsAuthenticated, IsTeacher],
        'partial_update': [IsAuthenticated, IsTeacher],
        'destroy': [IsAuthenticated, IsTeacher],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return LectureReadSerializer if self.request.method == 'GET' else LectureSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        user = self.request.user
        if user.is_superuser:
            return Lecture.objects.all()
        if user.user_type == 1:
            return Lecture.objects.filter(course__teachers=user,
                                          course=course_id)
        else:
            return Lecture.objects.filter(course__students=user,
                                          course=course_id)


class TaskViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a task.
    """
    queryset = Task.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsTeacher, ],
        'update': [IsAuthenticated, IsTeacher, ],
        'partial_update': [IsAuthenticated, IsTeacher, ],
        'destroy': [IsAuthenticated, IsTeacher, ],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return TaskReadSerializer if self.request.method == 'GET' else TaskSerializer

    def get_queryset(self):
        user = self.request.user
        lecture_id = self.kwargs['lecture_id']
        if user.is_superuser:
            return Task.objects.all()
        if user.user_type == 1:
            return Task.objects.filter(lecture__course__teachers=user,
                                       lecture=lecture_id)
        else:
            return Task.objects.filter(lecture__course__students=user,
                                       lecture=lecture_id)


class HomeworkViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a homework.
    """
    queryset = Homework.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsStudent],
        'update': [IsAuthenticated, IsStudent, IsAuthor],
        'partial_update': [IsAuthenticated, IsStudent, IsAuthor],
        'destroy': [IsAuthenticated, IsTeacher],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return HomeworkReadSerializer if self.request.method == 'GET' else HomeworkSerializer

    def get_queryset(self):
        user = self.request.user
        task_id = self.kwargs['task_id']
        if user.is_superuser:
            return Homework.objects.all()
        if user.user_type == 1:
            return Homework.objects.filter(task__lecture__course__teachers=user,
                                           task_id=task_id)
        else:
            return Homework.objects.filter(author=user,
                                           task_id=task_id)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response(status=status.HTTP_403_FORBIDDEN) ################################### DOBAVIT OPISANIE



class MarkViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a mark.
    """
    queryset = Mark.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsTeacher],
        'update': [IsAuthenticated, IsTeacher],
        'partial_update': [IsAuthenticated, IsTeacher],
        'destroy': [IsAuthenticated, IsTeacher],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return MarkReadSerializer if self.request.method == 'GET' else MarkSerializer

    def get_queryset(self):
        user = self.request.user
        homework_id = self.kwargs['homework_id']
        if user.is_superuser:
            return Mark.objects.all()
        if user.user_type == 1:
            return Mark.objects.filter(homework__task__lecture__course__teachers=user,
                                       homework_id=homework_id)
        else:
            return Mark.objects.filter(homework__author=user,
                                       homework_id=homework_id)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a comment.
    """
    queryset = Comment.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, ],
        'update': [IsAuthenticated, IsAuthor],
        'partial_update': [IsAuthenticated, IsAuthor],
        'destroy': [IsAuthenticated, IsAuthor],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return CommentReadSerializer if self.request.method == 'GET' else CommentSerializer

    def get_queryset(self):
        user = self.request.user
        mark_id = self.kwargs['mark_id']
        if user.is_superuser:
            return Comment.objects.all()
        if user.user_type == 1:
            return Comment.objects.filter(mark__homework__task__lecture__course__teachers=user,
                                          mark_id=mark_id)
        else:
            return Comment.objects.filter(mark__homework__task__lecture__course__students=user,
                                          mark_id=mark_id)
