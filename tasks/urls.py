from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="lists"),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('deletions/<str:pk>/', views.deleteTask, name="deletions")
]