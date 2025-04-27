from django.contrib import admin
from .models import Teacher, Category, Course, Group, Module, Homework, Student


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'username', 'image')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('phone_number',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  
    search_fields = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'duration', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'teacher', 'status', 'started_at', 'ended_at')
    list_filter = ('status', 'teacher', 'course')
    search_fields = ('name',)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'is_given')
    list_filter = ('group', 'is_given')
    search_fields = ('title',)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('overview', 'file', 'deadline', 'module')
    list_filter = ('module',)
    search_fields = ('overview',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'phone_number', 'student_code', 'group', 'status')
    search_fields = ('first_name', 'last_name', 'student_code', 'phone_number')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Student, StudentAdmin)
