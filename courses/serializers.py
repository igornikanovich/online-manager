from rest_framework import serializers

from .models import Course, Task, Homework, Mark, Comment, Lecture


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lecture
        fields = ('author', 'theme', 'file',)

    def create(self, validated_data):
        course_id = self.context.get('request').parser_context['kwargs']['course_id']
        validated_data['course'] = Course.objects.get(pk=course_id)
        return Lecture.objects.create(**validated_data)


class LectureReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'author', 'course', 'theme', 'file',)


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ('author', 'name', 'task',)

    def create(self, validated_data):
        lecture_id = self.context.get('request').parser_context['kwargs']['lecture_id']
        validated_data['lecture'] = Lecture.objects.get(pk=lecture_id)
        return Task.objects.create(**validated_data)


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'author', 'lecture', 'name', 'task',)


class HomeworkSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Homework
        fields = ('author', 'file',)

    def create(self, validated_data):
        task_id = self.context.get('request').parser_context['kwargs']['task_id']
        validated_data['task'] = Task.objects.get(pk=task_id)
        return Homework.objects.create(**validated_data)


class HomeworkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'author', 'task', 'file',)


class MarkSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    mark = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Mark
        fields = ('author', 'mark',)

    def create(self, validated_data):
        homework_id = self.context.get('request').parser_context['kwargs']['homework_id']
        validated_data['homework'] = Homework.objects.get(pk=homework_id)
        return Mark.objects.create(**validated_data)


class MarkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('id', 'author', 'homework', 'mark',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('author', 'comment',)

    def create(self, validated_data):
        mark_id = self.context.get('request').parser_context['kwargs']['mark_id']
        validated_data['mark'] = Mark.objects.get(pk=mark_id)
        return Comment.objects.create(**validated_data)


class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'mark', 'comment',)
