from django.contrib import admin

from goshuin_books.models import GoshuinBooks, Goshuins

admin.site.register([GoshuinBooks, Goshuins])
