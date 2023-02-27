from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    path('', views.HomeView.as_view(), name='home'),


]