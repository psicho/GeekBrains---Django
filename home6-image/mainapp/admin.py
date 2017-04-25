from django.contrib import admin
from .models import Teach, Work, Hobby

class WorkAdmin(admin.ModelAdmin):
    list_display = ['organization', 'region', 'image']

class TeachAdmin(admin.ModelAdmin):
    list_display = ['universitet', 'specials', 'image']

class HobbyAdmin(admin.ModelAdmin):
    list_display = ['hobbyname', 'image']

admin.site.register(Teach, TeachAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Hobby, HobbyAdmin)