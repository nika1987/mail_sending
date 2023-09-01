from django.shortcuts import render
from random import sample
from mail_sending.models import Message, Mailing, Log
from client.models import Client
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


'''ГЛАВНАЯ'''


def index(request):
    '''Главная страница'''
    total_mailings = Mailing.objects.count()  # всего рассылок
    # active_mailings = Mailing.objects.filter(status='running').count()  # всего активных рассылок
    unique_clients = Client.objects.distinct().count()  # всего уникальных клиентов
    all_posts = Blog.objects.filter(is_published=True)  # все блог-посты

    if len(all_posts) >= 3:
        random_posts = sample(list(all_posts), 3)  # 3 случайных блог-поста
    elif len(all_posts) == 0:
        random_posts = None
    else:
        random_posts = sample(list(all_posts), 1)

    context = {'total_mailings': total_mailings,
               # 'active_mailings': active_mailings,
               'unique_clients': unique_clients,
               'posts': random_posts}

    return render(request, 'mail_sending/index.html', context)
