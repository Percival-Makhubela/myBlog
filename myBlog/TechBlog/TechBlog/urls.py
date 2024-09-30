from django.urls import path
from .views import article_list, article_detail, article_create, article_edit, article_delete
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', article_list, name='article_list'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/new/', article_create, name='article_create'),
    path('article/<int:pk>/edit/', article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
]
