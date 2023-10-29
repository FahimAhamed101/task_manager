from django.contrib import admin
from .models import Tasks,Image
# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description','completed','priority','due_date','created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description','completed','priority','due_date',]
    ordering = ['priority']
    class Meta:
        model = Tasks


admin.site.register(Tasks,TasksAdmin)
admin.site.register(Image)