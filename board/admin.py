from django.contrib import admin
from .models import host, check, correction
# Register your models here.

admin.site.register(host)
admin.site.register(check)
admin.site.register(correction)
