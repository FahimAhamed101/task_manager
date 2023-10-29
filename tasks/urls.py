from django.urls import path,include
from .views import ListTasks,CreatTask,DetailTask
app_name = "tasks"
urlpatterns = [path('', ListTasks.as_view(), name='tasks'),
                  path('create-task/',CreatTask.as_view(), name='create-task'),
                  path('<int:pk>',DetailTask.as_view(), name='task'),
              ]