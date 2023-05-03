from .models import Client, Artist, Work
from django.contrib import admin

# Register your models here.

admin.site.register(Client)
admin.site.register(Artist)
admin.site.register(Work)
