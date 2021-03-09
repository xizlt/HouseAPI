from django.contrib import admin

from option.models import *


@admin.register(ParameterType)
class ParameterTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


class Base(admin.ModelAdmin):
    list_display = ('title', 'value')
    fields = ('title', 'value',)
    list_editable = ('value',)


admin.site.register(ElectroNight, Base)
admin.site.register(ElectroDay, Base)
admin.site.register(Gas, Base)
admin.site.register(HotWater, Base)
admin.site.register(CoolWater, Base)
