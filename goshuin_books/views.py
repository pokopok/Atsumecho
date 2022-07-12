from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from .models import GoshuinBooks, Goshuins
import os
from datetime import date

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
        form.fields['name'].label = 'ご朱印帳の名前'
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
        qs = qs.filter(goshuin_book=self.kwargs['book_id'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(GoshuinBooks, id=self.kwargs['book_id'])
        context['book_name'] = book.name 
        return context

class GoshuinAddView(CreateView):
    model = Goshuins
    fields = ['name', 'date', 'picture', 'memo']
    template_name = os.path.join('goshuin_books', 'add_goshuin.html')
    # success_url = reverse_lazy('goshuin_books:list_book')

    def get_success_url(self):
        return reverse('goshuin_books:book', kwargs={'book_id': self.object.goshuin_book.id})

    def form_valid(self, form): #フォーム送信前に実行される
        form.instance.goshuin_book = get_object_or_404(GoshuinBooks, id=self.kwargs['book_id'])
        return super(GoshuinAddView, self).form_valid(form)

    def get_form(self):
        form = super(GoshuinAddView, self).get_form()
        form.fields['name'].label = 'ご朱印の名前'
        form.fields['date'].label = '日付'
        form.fields['picture'].label = '写真'
        form.fields['date'].initial = date.today()
        return form