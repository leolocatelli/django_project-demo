from django.urls import path
from .views import (
    PostlistView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView #Imported the PostDeleteView class from views.py
)
from .import views

urlpatterns = [
    path('', PostlistView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Added in new url pattern
    path('about/',views.about, name='blog-about'),
]