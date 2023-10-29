from django.urls import path,include
from .views import ListTasks,CreatTask
app_name = "tasks"
urlpatterns = [path('', ListTasks.as_view(), name='tasks'),
                  path('create-task/',CreatTask.as_view(), name='create-task'),
              ]