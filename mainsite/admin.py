from django.contrib import admin

# Register your models here.
from .models import History, Number

admin.site.register(History)
admin.site.register(Number)
