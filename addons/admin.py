from django.contrib import admin
from addons.models import Addon, Category, AddonCategory


class AddonCategoryInline(admin.TabularInline):
    model = AddonCategory
    extra = 1
    

class AddonAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }
    inlines = (AddonCategoryInline,)
    
admin.site.register(Addon, AddonAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }
    inlines = (AddonCategoryInline,)
    
admin.site.register(Category, CategoryAdmin)

