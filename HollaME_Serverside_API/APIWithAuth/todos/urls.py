from django.urls import path
from .views import TodoListCreateAPI, TodoDetailAPI

urlpatterns = [
    path('todos/', TodoListCreateAPI.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailAPI.as_view(), name='todo-detail'),
]