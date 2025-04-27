from rest_framework import serializers
from .models import Category, Course, Student, Module, Homework


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Course
        fields = ['__all__']
        
class StudentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'phone_number', 'student_code', 'image']
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_url(obj.image.url)
        return None


class ModuleSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()  
    class Meta:
        model = Module
        fields = ['id', 'title', 'group', 'is_given']

class HomeworkSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True) 

    class Meta:
        model = Homework
        fields = ['id', 'overview', 'file', 'deadline', 'module']