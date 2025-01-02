from django.urls import path
from .views import (
    UserProfileListView, UserProfileDetailView, UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView,
    PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView,
    ForumListView, ForumDetailView, ForumCreateView, ForumUpdateView, ForumDeleteView,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # UserProfile URLs
    path('userprofiles/', UserProfileListView.as_view(), name='userprofile_list'),
    path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile_detail'),
    path('userprofiles/create/', UserProfileCreateView.as_view(), name='userprofile_create'),
    path('userprofiles/<int:pk>/update/', UserProfileUpdateView.as_view(), name='userprofile_update'),
    path('userprofiles/<int:pk>/delete/', UserProfileDeleteView.as_view(), name='userprofile_delete'),

    # Pet URLs
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('pets/create/', PetCreateView.as_view(), name='pet_create'),
    path('pets/<int:pk>/update/', PetUpdateView.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),

    # Forum URLs
    path('forums/', ForumListView.as_view(), name='forum_list'),
    path('forums/<int:pk>/', ForumDetailView.as_view(), name='forum_detail'),
    path('forums/create/', ForumCreateView.as_view(), name='forum_create'),
    path('forums/<int:pk>/update/', ForumUpdateView.as_view(), name='forum_update'),
    path('forums/<int:pk>/delete/', ForumDeleteView.as_view(), name='forum_delete'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
