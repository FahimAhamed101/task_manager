from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import  Tasks,Image
from .models import User
from django.views.generic.list import ListView
from .forms import TaskForm,ImageForm,UserRegisterForm
# Create your views here.

def RegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user = form.save() # new_user.email
            username = form.cleaned_data.get("username")
            # username = request.POST.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully.")
            # new_user = authenticate(username=form.cleaned_data.get('email'))
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("tasks:tasks")
    
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("tasks:tasks")


    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "sign-up.html", context)


def LoginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None: # if there is a user
                login(request, user)
                messages.success(request, "You are logged.")
                return redirect("tasks:tasks")
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect("sign-in")
        except:
            messages.warning(request, "User does not exist")

    if request.user.is_authenticated:
        messages.warning(request, "You are already logged In")
        return redirect("tasks:tasks")
        
    return render(request, "sign-in.html")

def logoutView(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("sign-in")
    
    
class ListTasks(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = "task_list.html"
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        
        return context
    
    
class CreatTask(CreateView):
    
    success_url = reverse_lazy('tasks:tasks')
    template_name = "tasks_creation.html"
    form_class = TaskForm
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('uid')
        instance = Tasks.objects.get_by_id(pk)
        if instance is None:
            raise Http404("tasks not exists")
        return instance
    def form_valid(self, form):
        pk = self.kwargs.get('uid')
        
        current_user = self.request.user
        if current_user.is_authenticated:
                if self.request.method == "POST":
                    form = TaskForm(self.request.POST)
                    files = self.request.FILES.getlist("image")
                    print(files)
                    if form.is_valid():
                        f = form.save(commit=False)
                        f.user = current_user 
                        f.save()
                        for i in files:
                            Image.objects.create(tasks=f, image=i)
                
            
                    else:
                        print(form.errors)
                else:
                    form = TaskForm()
                    imageform = ImageForm()
        else:
                if self.request.method == "POST":
                    form = TaskForm(self.request.POST)
                    files = self.request.FILES.getlist("image")
                    print(files)
                    if form.is_valid():
                        f = form.save(commit=False)
                        f.user = User.objects.create() 
                        f.save()
                        for i in files:
                            Image.objects.create(tasks=f, image=i)
                    
                    
                    if form.is_valid():
                        f = form.save(commit=False)
                        
                        f.save()
                        
                
            
                    else:
                        print(form.errors)
                else:
                    form = TaskForm()
                    imageform = ImageForm()
        return super(CreatTask, self).form_valid(form)
    
    