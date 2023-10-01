from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'robot_name')
    list_display_links = ('id', 'robot_name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("robot_name",)}

admin.site.register(License, LicenseAdmin)
