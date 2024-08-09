from django.urls import path
from . import views
from .views import AddPostView,AddCategoryView, LikeView, AddCommentView

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_details, name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:cats>/', views.category_view, name='category'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/comment',AddCommentView.as_view(), name='comment')
]
