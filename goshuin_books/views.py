from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import GoshuinBooks, Goshuins
import os

class GoshuinBookCreateView(CreateView):
    model = GoshuinBooks
    fields = ['name',]
    template_name = os.path.join('goshuin_books', 'create_book.html')
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form): #フォーム送信前に実行される
        form.instance.user = self.request.user
        return super(GoshuinBookCreateView, self).form_valid(form)

    def get_form(self):
        form = super(GoshuinBookCreateView, self).get_form()
        form.fields['name'].label = '御朱印帳の名前'
        return form

class GoshuinBookListView(ListView):
    model = GoshuinBooks
    template_name = os.path.join('goshuin_books', 'list_book.html')

    def get_queryset(self):
        qs = super(GoshuinBookListView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class GoshuinListView(ListView):
    model = Goshuins
    template_name = os.path.join('goshuin_books', 'book.html')

    def get_queryset(self):
        qs = super(GoshuinListView, self).get_queryset()
        qs = qs.filter(goshuin_book=self.kwargs['book'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(GoshuinBooks, id=self.kwargs['book'])
        context['book_name'] = book.name 
        return context