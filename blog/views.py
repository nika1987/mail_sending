from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.forms import BlogForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''CREATE - создается запись блога'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_index')
    permission_required = 'blog.add_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    '''READ - чтение списка записей блога'''

    model = Blog
    template_name = 'blog/blog_index.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    '''READ - чтение одной записи блога'''

    model = Blog
    success_url = reverse_lazy('blog:blog_detail')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''UPDATE - обновление записи блога'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_index')
    permission_required = 'blog.change_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''DELETE - удаление записи блога'''
    '''LoginRequiredMixin - скрывает контент от неавторизованных пользователей'''
    '''PermissionRequiredMixin - доступ к изменению контента, permission_required = приложение.команда_модель'''

    model = Blog
    success_url = reverse_lazy('blog:blog_index')
    permission_required = 'blog.delete_blog'
