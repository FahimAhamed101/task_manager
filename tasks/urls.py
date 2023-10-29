from django.urls import path,include
from .views import ListTasks
app_name = "tasks"
urlpatterns = [path('', ListTasks.as_view(), name='tasks'),
              ]