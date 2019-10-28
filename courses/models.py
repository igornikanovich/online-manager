from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models

from authentication.models import Student, Teacher
from courses.utils import content_file_name, content_file_answer


class Course(models.Model):
    author = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64, unique=True)
    teachers = models.ManyToManyField(Teacher, related_name='teachers', blank=True)
    students = models.ManyToManyField(Student, related_name='students', blank=True)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    theme = models.CharField(max_length=256, unique=True)
    file = models.FileField(upload_to=content_file_name, validators=[FileExtensionValidator(['PPTX', 'PPT'])])

    def __str__(self):
        return self.theme


class Task(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    task = models.TextField()

    def __str__(self):
        return self.name


class Homework(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to=content_file_answer)

    def __str__(self):
        return str(self.file)


class Mark(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(10)]) # ????????????????????????

    def __str__(self):
        return str(self.mark)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
