from django.urls import path,include
from .views import *
app_name = "tasks"
urlpatterns = [path('', ListTasks.as_view(), name='tasks'),
                  path('create-task/',CreatTask.as_view(), name='create-task'),
                  path('<int:pk>',DetailTask.as_view(), name='task'),
                  path('edit-task/<int:pk>',EditTask.as_view(), name='edit-task'),
               
                 path('delete-task/<int:pk>',DeleteTask.as_view(), name='delete-task'),
                 path('api/',ListTasksapi.as_view(), name='tasksapi'),
                 path('api/create/',CreateListTasksapi.as_view(), name='taskscreate'),
                 path('api/update/<int:pk>',UpadateListTasksapi.as_view(), name='tasksupdate'),
                 path('api/delete/<int:pk>',DeleteListTasksapi.as_view(), name='tasksdelete'),
              ]