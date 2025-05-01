from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CategoryListCreateApiView,
    CategoryDetailApiView,
    CourseListCreateApiView,
    StudentGenericApiView,
    CourseListByCategory,
    HomeworkCreateAPIView,
    VideoGenericApiView,
)

urlpatterns = [
    # Category Urls
    path('categories/', CategoryListCreateApiView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail'),

    # Course Url
    path('courses/', CourseListCreateApiView.as_view(), name='course_list_create'),

    # Course by Category Url
    path('courses/category/<int:category_id>/', CourseListByCategory.as_view(), name='course_list_by_category'),

    # Student Url
    path('students/', StudentGenericApiView.as_view(), name='student_list'),

    # Homework Url
    path('homework/', HomeworkCreateAPIView.as_view(), name='homework_create'),
    
    # Video Urls
    path('videos/', VideoGenericApiView.as_view(), name='video_create'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
