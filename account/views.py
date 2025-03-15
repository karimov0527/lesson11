from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm,EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect("home")
#     else:
#         form = RegisterForm()
#     return render(request, "register.html", {'form': form})

class Register(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})
    
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("home")
        return render(request, "register.html", {'form': form})
    
    
        
        





# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = LoginForm()
#     return render(request, "login.html", {'form': form})

class Login(View):
    def get(self,request):
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    
    def post(self,request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        return render(request, "login.html", {'form': form})
        


def logout_user(request):
    logout(request)
    return redirect('account:login')

class Profile(LoginRequiredMixin,View):
    login_url = 'account:login'
    def get(self, request):
        user = request.user  
        return render(request, 'profile.html', {'user': user})
        
class User_edit(View):
    def get(self,request):
        user = request.user 
        form = EditProfileForm(instance=user)
        return render(request,"user_edit.html",{"form":form})
    
    def post(self,request):
        user = request.user
        form = EditProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect("account:profile")
        return render(request,"user_edit.html",{"form":form})
    
    
    
