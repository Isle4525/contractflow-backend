from django.urls import path
from tasks.views import TaskListCreateView, TaskDetailView, TaskAcceptView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='tasks'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:id>/accept/', TaskAcceptView.as_view(), name='task-accept'),
]