from django.shortcuts import render
from client.models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from client.forms import ClientForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''CREATE - создается карточка клиента'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_index')
    permission_required = 'client.add_client'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    '''READ - чтение списка клиентов'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''

    model = Client
    template_name = 'client/client_index.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    '''READ - чтение одной записи клиента'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''

    model = Client
    success_url = reverse_lazy('client:client_detail')


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''UPDATE - обновление записи клиента'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_index')
    permission_required = 'client.change_client'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''DELETE - удаление записи клиента'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Client
    success_url = reverse_lazy('client:client_index')
    permission_required = 'client.delete_client'
