from django.contrib import admin

from .models import Course, Homework, Task, Mark, Comment, Lecture


admin.site.register(Course)
admin.site.register(Homework)
admin.site.register(Task)
admin.site.register(Mark)
admin.site.register(Comment)
admin.site.register(Lecture)
