from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ['method', 'path', 'timestamp']
    list_filter = ['method']
    search_fields = ['method', 'path', 'query', 'body']
    readonly_fields = ['timestamp']
    fieldsets = (
        ('Request Details', {
            'fields': ('method', 'path', 'query', 'body')
        }),
        ('Additional Info', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Log, LogAdmin)

# Register your models here.
