from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from .models import Books, Records
import os
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Books
    fields = ['name',]
    template_name = os.path.join('atsumecho', 'create_book.html')

    def get_success_url(self):
        form = super(BookCreateView, self).get_form()
        return reverse('atsumecho:book', kwargs={'book_id': form.instance.id})

    def form_valid(self, form): #フォーム送信前に実行される
        form.instance.user = self.request.user
        return super(BookCreateView, self).form_valid(form)

    def get_form(self):
        form = super(BookCreateView, self).get_form()
        form.fields['name'].label = 'あつめ帳名'
        return form


class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = os.path.join('atsumecho', 'list_book.html')

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class RecordListView(LoginRequiredMixin, ListView):
    model = Records
    template_name = os.path.join('atsumecho', 'book.html')

    def get(self, request, *args, **kwargs):
        book_user = get_object_or_404(Books, id=self.kwargs['book_id']).user
        # ログインユーザー自身が作成したあつめ帳でなければホームへ
        if not request.user == book_user:
            return redirect('accounts:home')
        return super().get(request,  *args, **kwargs)


    def get_queryset(self):
        qs = super(RecordListView, self).get_queryset()
        qs = qs.filter(book=self.kwargs['book_id'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Books, id=self.kwargs['book_id'])
        context['book_name'] = book.name
        context['book_id'] = self.kwargs['book_id']
        return context


class RecordAddView(LoginRequiredMixin, CreateView):
    model = Records
    fields = ['name', 'date', 'picture', 'memo']
    template_name = os.path.join('atsumecho', 'add_record.html')

    def get(self, request, *args, **kwargs):
        book_user = get_object_or_404(Books, id=self.kwargs['book_id']).user
        # ログインユーザー自身が作成したあつめ帳でなければホームへ
        if not request.user == book_user:
            return redirect('accounts:home')
        return super().get(request,  *args, **kwargs)

    def get_success_url(self):
        return reverse('atsumecho:book', kwargs={'book_id': self.object.book.id})

    def form_valid(self, form): #フォーム送信前に実行される
        form.instance.book = get_object_or_404(Books, id=self.kwargs['book_id'])
        return super(RecordAddView, self).form_valid(form)

    def get_form(self):
        form = super(RecordAddView, self).get_form()
        form.fields['name'].label = 'タイトル'
        form.fields['date'].label = '日付'
        form.fields['picture'].label = '写真'
        form.fields['date'].initial = date.today()
        return form


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Books
    template_name = os.path.join('atsumecho', 'delete_book.html')
    success_url = reverse_lazy('atsumecho:list_book')

    def get(self, request, *args, **kwargs):
        book_user = get_object_or_404(Books, id=self.kwargs['pk']).user
        # ログインユーザー自身が作成したあつめ帳でなければホームへ
        if not request.user == book_user:
            return redirect('accounts:home')
        return super().get(request, *args, **kwargs)


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Records
    template_name = os.path.join('atsumecho', 'delete_record.html')

    def get(self, request, *args, **kwargs):
        book_user = get_object_or_404(Records, id=self.kwargs['pk']).book.user
        # ログインユーザー自身が作成した記録でなければホームへ
        if not request.user == book_user:
            return redirect('accounts:home')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('atsumecho:book', kwargs={'book_id': self.object.book.id})


class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Books
    template_name = os.path.join('atsumecho', 'update_book.html')
    fields = ['name',]
    success_message = '更新しました'

    def get(self, request, *args, **kwargs):
        book_user = get_object_or_404(Books, id=self.kwargs['pk']).user
        # ログインユーザー自身が作成したあつめ帳でなければホームへ
        if not request.user == book_user:
            return redirect('accounts:home')
        return super().get(request, *args, **kwargs)

    def get_form(self):
        form = super(BookUpdateView, self).get_form()
        form.fields['name'].label = 'あつめ帳名'
        return form

    def get_success_url(self):
        return reverse_lazy('atsumecho:book', kwargs={'book_id': self.object.id})


class RecordUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Records
    template_name = os.path.join('atsumecho', 'update_record.html')
    fields = ['name', 'date', 'picture', 'memo']
    success_message = '更新しました'

    def get(self, request, *args, **kwargs):
        book_user = get_object_or_404(Records, id=self.kwargs['pk']).book.user
        # ログインユーザー自身が作成した記録でなければホームへ
        if not request.user == book_user:
            return redirect('accounts:home')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('atsumecho:book', kwargs={'book_id': self.object.book.id})

    def get_form(self):
        form = super(RecordUpdateView, self).get_form()
        form.fields['name'].label = 'タイトル'
        form.fields['date'].label = '日付'
        form.fields['picture'].label = '写真'
        return form