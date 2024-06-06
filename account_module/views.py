from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from account_module.forms import RegisterForm, LoginForm



# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account_module/register_page.html', {'register_form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
        return render(request, 'account_module/register_page.html', {'register_form': form})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse(f'You are now logged in as {request.user.username}')
        form = LoginForm()
        return render(request, 'account_module/login-page.html', {'login_form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                form.add_error('username', 'Your username or password is incorrect')
                return render(request, 'account_module/login-page.html', {'login_form': form})



class LogoutView(View):
    def get(self, request):
        username = request.user.username
        if request.user.is_authenticated:
            logout(request)
            return HttpResponse(f'Dear {username}, you have successfully logged out')
        else:
            return redirect('account:login')
