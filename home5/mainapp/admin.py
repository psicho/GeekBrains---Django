from django.contrib import admin
from .models import Teach, Work, Hobby

class WorkAdmin(admin.ModelAdmin):
    list_display = ['organization', 'region']

class TeachAdmin(admin.ModelAdmin):
    list_display = ['universitet', 'specials']

class HobbyAdmin(admin.ModelAdmin):
    list_display = ['hobbyname']

admin.site.register(Teach, TeachAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Hobby, HobbyAdmin)