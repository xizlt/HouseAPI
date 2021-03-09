from django.contrib import admin

from reservation.models import Reservation, TypeReservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('type', 'executed', 'data_begin', 'data_end', 'created',)
    readonly_fields = ('created', 'update')
    list_filter = ('type', 'executed', 'data_begin',)
    fieldsets = (
        ('Date', {
            'fields': (('data_begin', 'data_end',),)
        }),
        (None, {
            'fields': ('type', 'executed', 'user',)
        }),
    )


@admin.register(TypeReservation)
class TypeReservationAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('title',)
    fields = ('title',)
