from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('profile',views.profile, name='profile'),
    path('password',views.ChangePasswordView.as_view(), name='password'),
]