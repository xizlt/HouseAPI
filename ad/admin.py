from django.contrib import admin

from ad.models import Ad, TypeAd


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    radio_fields = {'type': admin.HORIZONTAL}
    save_on_top = True
    list_display = ('title', 'type', 'beginning', 'ending', 'created',)
    readonly_fields = ('created',)
    search_fields = ('title', )
    list_filter = ('created', 'beginning', 'ending', 'title', 'type',)
    fieldsets = (
        ('Date', {
            'fields': (('beginning', 'ending',),)
        }),
        (None, {
            'fields': ('type', 'title', 'text',)
        }),
        ('User information', {
            'classes': ('collapse',),
            'fields': ('user',),
        }),
    )


@admin.register(TypeAd)
class TypeAdAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('title',)
    fields = ('title',)
