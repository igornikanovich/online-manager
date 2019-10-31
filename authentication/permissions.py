from rest_framework import permissions

from courses.models import Course, Lecture, Task, Homework
from .models import User


ROLE_DEFAULT_MESSAGE = 'Only {}s are allowed to view and modify this content.'
AUTHOR_DEFAULT_MESSAGE = 'You should be the author of this content in order to modify it.'


class IsTeacher(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('teacher')

    def has_permission(self, request, view):
        return request.user.user_type == 1


class IsStudent(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('student')

    def has_permission(self, request, view):
        return request.user.user_type == 2


class IsAuthor(permissions.BasePermission):
    message = AUTHOR_DEFAULT_MESSAGE

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
