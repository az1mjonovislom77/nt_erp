from django.contrib import admin
from .models import Category, Course, Student, Teacher, Group, Module, Homework, Video

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'duration')
    search_fields = ('name', 'category__name')  

admin.site.register(Course, CourseAdmin)


# Teacher Admin
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'phone_number')
    search_fields = ('first_name', 'last_name', 'username')

admin.site.register(Teacher, TeacherAdmin)


# Student Admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'student_code', 'group', 'gender', 'status')
    search_fields = ('first_name', 'last_name', 'student_code', 'group__name')

admin.site.register(Student, StudentAdmin)


# Group Admin
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'teacher', 'started_at', 'ended_at', 'status')
    search_fields = ('name', 'course__name', 'teacher__username')

admin.site.register(Group, GroupAdmin)


# Module Admin
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'group', 'is_given')
    search_fields = ('title', 'group__name')

admin.site.register(Module, ModuleAdmin)


# Homework Admin
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'overview', 'module', 'deadline', 'created_at')
    search_fields = ('overview', 'module__title')

admin.site.register(Homework, HomeworkAdmin)


# Video Admin
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'module')
    search_fields = ('title', 'module__title')

admin.site.register(Video, VideoAdmin)

