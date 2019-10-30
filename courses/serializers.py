from rest_framework import serializers

from .models import Course, Task, Homework, Mark, Comment, Lecture


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('title', 'students', 'teachers')

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        students_data = validated_data.pop('students')
        teachers_data = validated_data.pop('teachers')
        course = Course.objects.create(author=author, **validated_data)

        for student in students_data:
            course.students.add(student)
        for teacher in teachers_data:
            course.teachers.add(teacher)
        return course


class CourseReadSerializer(CourseSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        # depth = 1


class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ('theme', 'file',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        course_id = self.context.get('request').parser_context['kwargs']['course_id']
        validated_data['course'] = Course.objects.get(pk=course_id)
        return Lecture.objects.create(author=author, **validated_data)


class LectureReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'author', 'course', 'theme', 'file',)
        # depth = 2


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'task',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        lecture_id = self.context.get('request').parser_context['kwargs']['lecture_id']
        validated_data['lecture'] = Lecture.objects.get(pk=lecture_id)
        return Task.objects.create(author=author, **validated_data)


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'author', 'lecture', 'name', 'task',)
        # depth = 1


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('file',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.student
        task_id = self.context.get('request').parser_context['kwargs']['task_id']
        validated_data['task'] = Task.objects.get(pk=task_id)
        return Homework.objects.create(author=author, **validated_data)


class HomeworkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'author', 'task', 'file',)
        # depth = 1


class MarkSerializer(serializers.ModelSerializer):

    mark = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Mark
        fields = ('mark',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user.teacher
        homework_id = self.context.get('request').parser_context['kwargs']['homework_id']
        validated_data['homework'] = Homework.objects.get(pk=homework_id)
        return Mark.objects.create(author=author, **validated_data)


class MarkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('id', 'author', 'homework', 'mark',)
        # depth = 1


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment',)

    def create(self, validated_data):
        request = self.context['request']
        author = request.user
        mark_id = self.context.get('request').parser_context['kwargs']['mark_id']
        validated_data['mark'] = Mark.objects.get(pk=mark_id)
        return Comment.objects.create(author=author, **validated_data)


class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'mark', 'comment',)
        # depth = 1
