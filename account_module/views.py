from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from account_module.forms import RegisterForm, LoginForm, ProfileForm, UserForm
from .models import UserInformation


# Create your views here.


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse('baraye sabt nam kharej shavid')
        form = RegisterForm()
        return render(request, 'account_module/register_page.html', {'register_form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Dear, {form.cleaned_data['username']} registered successfully")
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


@login_required
def profile(request):
    user = request.user
    user_information, created = UserInformation.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        user_information_form = ProfileForm(request.POST, request.FILES, instance=user_information)

        if user_form.is_valid() and user_information_form.is_valid():
            user_form.save()
            user_information_form.save()
            return redirect('account:profile')
    else:
        user_form = UserForm(instance=user)
        user_information_form = ProfileForm(instance=user_information)

    context = {
        'user_form': user_form,
        'user_information_form': user_information_form
    }

    return render(request, 'account_module/profile.html', context)

