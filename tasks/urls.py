from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.index, name="lists"),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('deletions/<str:pk>/', views.deleteTask, name="deletions"),
#     path('api/', include(router.urls)),
#     path('api/', views.api_root),
]
