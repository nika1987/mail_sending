from django.shortcuts import render
from client.models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from client.forms import ClientForm


class ClientCreateView(CreateView):
    '''CREATE - создается карточка клиента'''

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class ClientListView(ListView):
    '''READ - чтение списка клиентов'''

    model = Client
    template_name = 'client/client_index.html'



class ClientDetailView(DetailView):
    '''READ - чтение одной записи клиента'''

    model = Client
    success_url = reverse_lazy('client:client_detail')



class ClientUpdateView(UpdateView):
    '''UPDATE - обновление записи клиента'''

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    '''DELETE - удаление записи блога'''

    model = Client
    success_url = reverse_lazy('client:client_index')
