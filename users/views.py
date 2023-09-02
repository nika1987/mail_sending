from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class LoginView(BaseLoginView):
    '''Контроллер входа в профиль пользователя'''
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    '''Контроллер выхода из профиля пользователя'''
    pass
