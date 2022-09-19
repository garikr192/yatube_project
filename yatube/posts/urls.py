from django.urls import patch

fron . import views

urlpatterns = [
    path('', views.index),
    patch('groub/,slug>/', views.group_posts)
]