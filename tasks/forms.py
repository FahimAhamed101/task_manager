from django import forms
from .models import Tasks,Image,User
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Tasks
        fields = ['title', 'description','completed','priority','due_date','created_at']
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter description'
        self.fields['due_date'].widget.attrs['placeholder'] = 'Enter description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'text-black'

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(), required=False,
    )

    class Meta:
        model = Image
        fields = ("image",)