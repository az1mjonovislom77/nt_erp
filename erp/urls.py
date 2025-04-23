from django.urls import path
from .views import (
    CategoryListCreateAPIView, CategoryDetailAPIView,
    CourseListCreateAPIView, CourseDetailAPIView
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category_create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('courses/', CourseListCreateAPIView.as_view(), name='course_create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
]
