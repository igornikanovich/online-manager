from rest_framework import permissions

from .models import Course, Lecture

ROLE_DEFAULT_MESSAGE = 'Only {}s are allowed to view and modify this content.'


class IsTeacher(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('teacher')

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_type == 1


class IsStudent(permissions.BasePermission):
    message = ROLE_DEFAULT_MESSAGE.format('student')

    def has_permission(self, request, view):
        return request.user.user_type == 2


class IsAuthor(permissions.BasePermission):
    message = 'Only the author has the right to change the content'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsMember(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.author == request.user:
            return True
        if request.user.user_type == 1:
            if view.kwargs.get('course_id'):
                course_id = view.kwargs['course_id']
                return Course.objects.filter(teachers=request.user, id=course_id)
            elif view.kwargs.get('pk'):
                course_id = view.kwargs['pk']
                return Course.objects.filter(teachers=request.user, id=course_id)
        elif request.user.user_type == 2:
            if view.kwargs.get('course_id'):
                course_id = view.kwargs['course_id']
                return Course.objects.filter(students=request.user, id=course_id)
            elif view.kwargs.get('pk'):
                course_id = view.kwargs['pk']
                return Course.objects.filter(students=request.user, id=course_id)
