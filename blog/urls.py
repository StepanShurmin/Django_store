from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from config.urls import path

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', never_cache(BlogListView.as_view()), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('update/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
