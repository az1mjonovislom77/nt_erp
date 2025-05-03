from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from erp.models import Category, Course, Student, Homework, Teacher, Group, Module, Video
from .serializers import CategoryModelSerializer, CourseModelSerializer, StudentModelSerializer, HomeworkSerializer, TeacherSerializer, GroupSerializer, ModuleSerializer, VideoSerializer
from .permissions import CanEditWithinTwoHours, IsWorkingHours

class BaseListApiView(GenericAPIView):
    def get_serializer_data(self, queryset, serializer_class):
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


class CategoryListCreateApiView(BaseListApiView, ListCreateAPIView):
    queryset = Category.objects.all().annotate(course_count=Count('courses'))
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAuthenticated]


class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'pk'


class CourseListCreateApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


class CourseListByCategory(BaseListApiView):
    serializer_class = CourseModelSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Course.objects.filter(category=category_id) if category_id else Course.objects.none()

    def get(self, request, *args, **kwargs):
        courses = self.get_queryset()
        return self.get_serializer_data(courses, self.serializer_class)


class StudentGenericApiView(BaseListApiView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.get_serializer_data(self.get_queryset(), self.serializer_class)


class HomeworkCreateAPIView(CreateAPIView):
    permission_classes = [CanEditWithinTwoHours]
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()


class TeacherGenericApiView(BaseListApiView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.get_serializer_data(self.get_queryset(), self.serializer_class)


class GroupGenericApiView(BaseListApiView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        return self.get_serializer_data(self.get_queryset(), self.serializer_class)


class ModuleGenericApiView(BaseListApiView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get(self, request, *args, **kwargs):
        return self.get_serializer_data(self.get_queryset(), self.serializer_class)


class VideoListCreateAPIView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'pk'

