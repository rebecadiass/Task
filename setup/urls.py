from django.contrib import admin
from django.urls import path
from tasks.views import TaskListView, TaskCreateView, TaskDeleteView, complete_task

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task_list"),
    path("create", TaskCreateView.as_view(), name="task_create"),
    path("delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
     path("complete/<int:pk>", complete_task, name="task_complete"),
]
    
