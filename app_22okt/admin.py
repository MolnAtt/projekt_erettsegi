from django.contrib import admin

from .models import Festo, Kep

# Register your models here.

admin.site.register(Festo)
admin.site.register(Kep)