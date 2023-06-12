from django.contrib import admin

# Register your models here.
from .models import History, Number, Winners, Bombed

admin.site.register(History)
admin.site.register(Number)
admin.site.register(Winners)
admin.site.register(Bombed)
