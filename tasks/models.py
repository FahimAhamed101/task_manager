from django.db import models
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from django.contrib.auth.models import UserManager
from django.conf import settings
# Create your models here.
from django.utils import timezone

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):   
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()
    class Meta:
        app_label = 'tasks'
    def __str__(self):
        return self.username 
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class Tasks(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True )
                              
    title= models.CharField(max_length=200)
    description= models.TextField(null=True,
                               blank=True)
    
    due_date = models.DateTimeField(default=timezone.now)
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
