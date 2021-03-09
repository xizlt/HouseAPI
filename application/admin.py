from django.contrib import admin

from application.models import Application, TypeApplication


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'executed', 'due_data', 'created',)
    readonly_fields = ('created',)
    list_filter = ('created', 'due_data', 'type',)


@admin.register(TypeApplication)
class TypeApplicationAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('title',)
    fields = ('title',)
