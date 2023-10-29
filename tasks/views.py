from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import  Tasks,Image
from .models import User
from django.views.generic.list import ListView
# Create your views here.

class Login(LoginView):
    template_name = "login.html"
    field = '__all__'
    def get_success_url(self):
        return reverse_lazy('tasks:tasks')


class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks:tasks')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)

        return super(Register,self).form_valid(form)

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks:tasks')
        return super(Register, self).get(*args, **kwargs)
    
    
class ListTasks(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = "task_list.html"
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        
        return context