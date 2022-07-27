from django.contrib import admin

from atsumecho.models import Books, Records

admin.site.register([Books, Records])
