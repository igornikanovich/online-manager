from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsTeacher, IsTeacherAuthor, IsStudent, IsUserAuthor, IsStudentAuthor
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
        'update': [IsAuthenticated, IsTeacher, IsTeacherAuthor],
        'partial_update': [IsAuthenticated, IsTeacher, IsTeacherAuthor],
        'destroy': [IsAuthenticated, IsTeacher, IsTeacherAuthor],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return CourseReadSerializer if self.request.method == 'GET' else CourseSerializer


class LectureViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a lecture.
    """
    queryset = Lecture.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsTeacher],
        'update': [IsAuthenticated, IsTeacher, IsTeacherAuthor],
        'partial_update': [IsAuthenticated, IsTeacher, IsTeacherAuthor],
        'destroy': [IsAuthenticated, IsTeacher, IsTeacherAuthor],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return LectureReadSerializer if self.request.method == 'GET' else LectureSerializer

    def get_queryset(self):
        return Lecture.objects.filter(course_id=self.kwargs['course_id'])


class TaskViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a task.
    """
    queryset = Task.objects.all()
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
        return TaskReadSerializer if self.request.method == 'GET' else TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(lecture__course_id=self.kwargs['course_id'],
                                   lecture_id=self.kwargs['lecture_id'])


class HomeworkViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a homework.
    """
    queryset = Homework.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, IsStudent],
        'update': [IsAuthenticated, IsStudent, IsStudentAuthor],
        'partial_update': [IsAuthenticated, IsStudent, IsStudentAuthor],
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
        return Homework.objects.filter(task__lecture__course_id=self.kwargs['course_id'],
                                       task__lecture_id=self.kwargs['lecture_id'],
                                       task_id=self.kwargs['task_id'])


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
        return Mark.objects.filter(homework__task__lecture__course_id=self.kwargs['course_id'],
                                   homework__task__lecture_id=self.kwargs['lecture_id'],
                                   homework__task_id=self.kwargs['task_id'],
                                   homework_id=self.kwargs['homework_id'])


class CommentViewSet(viewsets.ModelViewSet):
    """
    Endpoint for list, create, update and delete a comment.
    """
    queryset = Comment.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated, ],
        'retrieve': [IsAuthenticated, ],
        'create': [IsAuthenticated, ],
        'update': [IsAuthenticated, IsUserAuthor, ],
        'partial_update': [IsAuthenticated, IsUserAuthor],
        'destroy': [IsAuthenticated, IsUserAuthor],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        return CommentReadSerializer if self.request.method == 'GET' else CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(mark__homework__task__lecture__course_id=self.kwargs['course_id'],
                                      mark__homework__task__lecture_id=self.kwargs['lecture_id'],
                                      mark__homework__task_id=self.kwargs['task_id'],
                                      mark__homework_id=self.kwargs['homework_id'],
                                      mark_id=self.kwargs['mark_id'])
