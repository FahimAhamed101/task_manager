from django.db import models
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from django.conf import settings
# Create your models here.
from django.utils import timezone
class User(AbstractBaseUser):   
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    USERNAME_FIELD = "uid"
    class Meta:
        app_label = 'tasks' 
class Tasks(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True )
                              
    title= models.CharField(max_length=200)
    description= models.TextField(null=True,
                               blank=True)
    
    due_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['completed']
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def __str__(self):
        return str(self.title)
    
class Image(models.Model):
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE,related_name='images',verbose_name=('image'))
    image = models.ImageField(upload_to="images", blank=False, null=False)
    
    def __str__(self):
        return str(self.image)
