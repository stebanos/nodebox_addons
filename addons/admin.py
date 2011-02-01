from django.contrib import admin
from addons.models import Addon


class AddonAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }
    
admin.site.register(Addon, AddonAdmin)