from django.urls import path
from .views import BlogListCreate, BlogRetrieveUpdateDestroy, CategoryListCreate, CategoryRetrieveUpdateDestroy, PairFinding

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroy.as_view(), name='blog-detail'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('find-pair/', PairFinding.as_view(), name='find-pair'),
]
