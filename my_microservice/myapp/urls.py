from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),  # GET и POST для задач
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),  # GET, PUT, PATCH, DELETE для конкретной задачи
]