from django.contrib import admin

from meter.models import TypeMeter, Meter, Indication, ItemMeter


def getType(obj):
    return f"{obj.meter.type}"


getType.short_description = 'Type'


class IndicationInline(admin.TabularInline):
    model = Indication
    extra = 0
    fields = ('created', 'value')
    readonly_fields = ('created', )


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    inlines = (IndicationInline,)
    list_display = ('type', 'name',)
    readonly_fields = ('created',)
    list_filter = ('type',)
    fields = ('name', 'type',)
    date_hierarchy = 'created'


@admin.register(TypeMeter)
class TypeMeterAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    fields = ('title',)


@admin.register(Indication)
class IndicationAdmin(admin.ModelAdmin):
    list_display = ('meter', 'value', 'used', getType, 'created')
    search_fields = ('meter__name',)
    list_filter = ('meter', 'created')
    fields = ('meter', 'value', 'used')
    date_hierarchy = 'created'


@admin.register(ItemMeter)
class ItemMeterAdmin(admin.ModelAdmin):
    # inlines = (IndicationInline)
    list_display = ('meter', getType, 'user')
    search_fields = ('meter__name',)
    list_filter = ('meter', 'user')
    fields = ('meter', 'user')
