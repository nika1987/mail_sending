from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy, reverse
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm


class LoginView(BaseLoginView):
    '''Контроллер входа в профиль пользователя'''
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    '''Контроллер выхода из профиля пользователя'''
    pass


class RegisterView(CreateView):
    '''Контроллер регистрации пользователя'''
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    '''Профиль пользователя'''
    model = User
    form_class = UserProfileForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
