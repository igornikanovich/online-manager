from rest_framework import permissions

from courses.models import Course, Homework


class IsTeacher(permissions.BasePermission):
    message = 'Only teachers are allowed to view and modify this content.'

    def has_permission(self, request, view):
        return request.user.user_type == 1


class IsStudent(permissions.BasePermission):
    message = 'Only students are allowed to view and modify this content.'

    def has_permission(self, request, view):
        return request.user.user_type == 2


class IsAuthor(permissions.BasePermission):
    message = 'Only the author has the right to change the content'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsMember(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.user_type == 1:
            if view.kwargs.get('course_id'):
                course_id = view.kwargs['course_id']
                return Course.objects.filter(teachers=request.user, id=course_id)
            elif view.kwargs.get('pk'):
                course_id = view.kwargs['pk']
                return Course.objects.filter(teachers=request.user, id=course_id)
        if request.user.user_type == 2:
            if view.kwargs.get('homework_id'):
                homework_id = view.kwargs['homework_id']
                return Homework.objects.filter(author=request.user, id=homework_id)
