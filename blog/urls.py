from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_view, name='category'),
    path('article/', views.article_view, name='article'),
]