from django.urls import path,include
from .views import ListTasks,CreatTask,DetailTask,EditTask,DeleteTask
app_name = "tasks"
urlpatterns = [path('', ListTasks.as_view(), name='tasks'),
                  path('create-task/',CreatTask.as_view(), name='create-task'),
                  path('<int:pk>',DetailTask.as_view(), name='task'),
                  path('edit-task/<int:pk>',EditTask.as_view(), name='edit-task'),
               
                 path('delete-task/<int:pk>',DeleteTask.as_view(), name='delete-task')
              ]