from rest_framework import serializers
from erp.models import Category, Course, Student, Module, Homework, Teacher, Group, Video


class CourseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        exclude = ('is_given',)


class HomeworkSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Homework
        fields = '__all__'

    def save(self, **kwargs):
        homework = super().save(**kwargs)
        module = homework.module
        module.is_given = True  
        module.save()
        return homework


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    file_size = serializers.ReadOnlyField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'file', 'module', 'file_size']