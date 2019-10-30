from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from courses.models import Course, Lecture, Task
from .models import Student, Teacher


ROLE_DEFAULT_MESSAGE = 'Only {}s are allowed to view and modify this content.'
AUTHOR_DEFAULT_MESSAGE = 'You should be the author of this content in order to modify it.'


class IsStudent(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('student')

    def has_permission(self, request, view):
        return Student.objects.filter(user=request.user).exists()


class IsTeacher(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('teacher')

    def has_permission(self, request, view):
        return Teacher.objects.filter(user=request.user).exists()


class IsStudentAuthor(permissions.BasePermission):
    message = AUTHOR_DEFAULT_MESSAGE

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user.student


class IsTeacherAuthor(permissions.BasePermission):
    message = AUTHOR_DEFAULT_MESSAGE

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user.teacher


class IsUserAuthor(permissions.BasePermission):
    message = AUTHOR_DEFAULT_MESSAGE

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsMemberCourse(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('member')

    def has_permission(self, request, view):
        try:
            if request.user.student:
                return Course.objects.filter(students=request.user.student)
        except ObjectDoesNotExist:
            return Course.objects.filter(teachers=request.user.teacher)


class IsMemberLecture(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('member')

    def has_permission(self, request, view):
        try:
            if request.user.student:
                return Lecture.objects.filter(course__students=request.user.student)
        except ObjectDoesNotExist:
            return Lecture.objects.filter(course__teachers=request.user.teacher)


class IsMemberTask(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('member')

    def has_permission(self, request, view):
        try:
            if request.user.student:
                return Task.objects.filter(lecture__course__students=request.user.student)
        except ObjectDoesNotExist:
            return Task.objects.filter(lecture__course__teachers=request.user.teacher)


class IsMemberHomework(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('member')

    def has_permission(self, request, view):
        try:
            if request.user.student:
                return Course.objects.filter(task__lecture__course__students=request.user.student)
        except ObjectDoesNotExist:
            return Course.objects.filter(task__lecture__course__teachers=request.user.teacher)
