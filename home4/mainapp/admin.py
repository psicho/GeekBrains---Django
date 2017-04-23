from django.contrib import admin
from .models import Teach, Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ['organization', 'region']

class TeachAdmin(admin.ModelAdmin):
    list_display = ['universitet', 'specials']

admin.site.register(Teach, TeachAdmin)
admin.site.register(Work, WorkAdmin)