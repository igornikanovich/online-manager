from rest_framework import serializers

from .models import Course, Task, Homework, Mark, Comment, Lecture


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseReadSerializer(CourseSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        depth = 1


class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ('course', 'theme', 'file',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        return Lecture.objects.create(author=author, **validated_data)


class LectureReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'author', 'course', 'theme', 'file',)
        depth = 1


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('lecture', 'name', 'task',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        return Task.objects.create(author=author, **validated_data)


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'author', 'lecture', 'name', 'task',)
        depth = 1


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('homework', 'file',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.student
        return Homework.objects.create(author=author, **validated_data)


class HomeworkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'author', 'homework', 'file',)
        depth = 1


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = ('homework', 'mark',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        return Task.objects.create(author=author, **validated_data)


class MarkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('id', 'author', 'homework', 'mark',)
        depth = 1


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('mark', 'comment',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user
        return Task.objects.create(author=author, **validated_data)


class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'mark', 'comment',)
        depth = 1
