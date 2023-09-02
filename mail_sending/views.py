from django.shortcuts import render
from random import sample
from mail_sending.models import Message, Mailing, Log
from client.models import Client
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from mail_sending.forms import MailingForm, MessageForm

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


'''РАССЫЛКИ - Mailing'''


class MailingCreateView(CreateView):
    '''CREATE - создается карточка рассылки'''

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail_sending:mail_sending_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class MailingListView(ListView):
    '''READ - чтение списка рассылок'''

    model = Mailing
    template_name = 'mail_sending/mail_sending_index.html'


class MailingDetailView(DetailView):
    '''READ - чтение одной рассылки'''

    model = Mailing
    success_url = reverse_lazy('mail_sending:mail_sending_detail')


class MailingUpdateView(UpdateView):
    '''UPDATE - обновление записи рассылки'''

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail_sending:mail_sending_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mail_sending:mail_sending_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    '''DELETE - удаление записи рассылки'''

    model = Mailing
    success_url = reverse_lazy('mail_sending:mail_sending_index')



'''СООБЩЕНИЕ - Message'''

class MessageCreateView(CreateView):
    '''CREATE - создается сообщение'''

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_sending:message_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class MessageListView(ListView):
    '''READ - чтение списка сообщений'''

    model = Message
    template_name = 'mail_sending/message_index.html'


class MessageDetailView(DetailView):
    '''READ - чтение одного сообщения'''

    model = Message
    success_url = reverse_lazy('mail_sending:message_detail')


class MessageUpdateView(UpdateView):
    '''UPDATE - обновление сообщения'''

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_sending:message_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mail_sending:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    '''DELETE - удаление сообщения'''

    model = Message
    success_url = reverse_lazy('mail_sending:message_index')





'''ЛОГИ - log'''


